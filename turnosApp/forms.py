from cProfile import label

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
                attrs={'class': 'form-control m-2', 'type': 'date'}),
            'estado': forms.Select(
                attrs={'class': 'form-control m-2'}),
            'medico': forms.Select(
                attrs={'class': 'form-control dropdown m-2','placeholder':'Seleccione un medico'}),
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

class pacienteForm(forms.ModelForm):
    OPCIONES_CONTACTO = [
        (False, 'Teléfono'),
        (True, 'Email')
    ]

    class Meta:

        model = Paciente
        fields = ['nombre', 'ci', 'sexo', 'conacto', 'tipo_contacto',]
        exclude = [ 'id', 'status']
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control m-2'}),
            'ci': forms.TextInput(
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
