from datetime import date

from django import forms
from .models import *

# class especialidadesForm(forms.ModelForm):
#     class Meta:
#         model = Especialidad
#         fields = '__all__'

# class medicosForm(forms.ModelForm):
#     class Meta:
#         model = Medicos
#         fields = ['Nombre: ', 'Número de matriula:', 'Telefono: ']

class turnoForm(forms.ModelForm):
    class Meta:

        model = Turno
        fields = ['paciente','observaciones','fecha_turno','especialidad','medico']
        exclude = ['fecha_registro', 'id','status']
        widgets = {
            'paciente': forms.TextInput(
                attrs={'class': 'form-control m-2'}),
            'fecha_turno': forms.DateInput(
                attrs={'class': 'form-control m-2', 'type': 'date', 'min': date.today().isoformat()}),
            'estado': forms.Select(
                attrs={'class': 'form-control m-2'}),
            'medico': forms.Select(
                attrs={'class': 'form-control dropdown m-2','placeholder' : 'Seleccione un medico'}),
            'observaciones': forms.TextInput(
                attrs={'class': 'form-control m-2'}
            )
        }
        labels = {
            'medico' : 'Seleccione un médico',
            'paciente': 'Ingrese su codigo de paciente',
        }

    especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all(),
        empty_label= 'Seleccione una especialidad',
        widget=forms.Select(
            attrs={'class': 'form-control m-2 dropdown',
                   'id': 'especialidad',
                   'placeholder': 'Seleccione una especialidad'}
        ),
        required=True
    )
    def clean(self):
        cleaned_data = super().clean()
        paciente_ci = cleaned_data.get("paciente")
        fecha = cleaned_data.get("fecha_turno")
        medico_user = cleaned_data.get("medico")  # Ahora obtenemos el User asociado al médico

        if paciente_ci is None or fecha is None or medico_user is None:
            return cleaned_data  # Algún campo requerido no está presente aún

        try:
            paciente_obj = Paciente.objects.get(ci=paciente_ci)
        except Paciente.DoesNotExist:
            raise forms.ValidationError("El código de paciente introducido es incorrecto.")

        try:
            medico_obj = Medico.objects.get(user=medico_user)  # Obtenemos el objeto Medico usando el User
        except Medico.DoesNotExist:
            raise forms.ValidationError("El médico seleccionado no es válido.")

        if (Turno.objects.filter(
            paciente=paciente_obj,  # Usamos el objeto Paciente directamente
            fecha_turno=fecha,
            medico=medico_obj,      # Usamos el objeto Medico directamente
            status=0
        ).count() > 0):
            raise forms.ValidationError(
                f"El paciente {paciente_obj.ci} ya tiene un "
                f"turno con el médico {medico_obj.user.first_name} {medico_obj.user.last_name} para la "
                f"fecha seleccionada"
            )

        if fecha < date.today():
            raise forms.ValidationError("No puedes seleccionar una fecha pasada.")

        return cleaned_data

class pacienteForm(forms.ModelForm):
    OPCIONES_CONTACTO = [
        (False, 'Teléfono'),
        (True, 'Email')
    ]

    class Meta:

        model = Paciente
        fields = ['nombre', 'ci', 'sexo', 'conacto','ciudad', 'tipo_contacto',]
        exclude = [ 'id', 'status']
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control m-2'}),
            'ci': forms.TextInput(
                attrs={'class': 'form-control m-2'}),
            'ciudad': forms.TextInput(
                attrs={'class': 'form-control m-2'}),
            'sexo': forms.Select(
                attrs={'class': 'form-control m-2'}),
            'conacto': forms.TextInput(
                attrs={'class': 'form-control m-2'}),
        }
        labels = {
            'ci' : 'Número de cédula',
            'nro_seguro' : 'Número de seguro',
            'nro_telefono': 'Número de telefono',
            'sexo': 'Selecione su sexo',
        }

    tipo_contacto = forms.BooleanField(
        widget = forms.RadioSelect(
            choices=OPCIONES_CONTACTO,
            attrs={'class': 'm-2',
                   'type':'radio'}),
        required = True
    )

    def clean_ci(self):
        ci = self.cleaned_data.get("ci")
        if Paciente.objects.filter(ci = ci).exists():
            raise forms.ValidationError("Este número de cédula ya está registrado.")
        return ci