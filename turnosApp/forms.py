from django import forms
from .models import *

class especialidadesForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

# class medicosForm(forms.ModelForm):
#     class Meta:
#         model = Medicos
#         fields = ['Nombre: ', 'Número de matriula:', 'Telefono: ']

class turnoForm(forms.ModelForm):
    class Meta:

        model = Turno
        fields = ['nombre','ci','sexo','nro_telefono','ciudad','nro_seguro','fecha_turno','especialidad','medico']
        exclude = ['fecha_registro', 'id','status']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control m-2 ', 'placeholder': 'Nombre del paciente'}),
            'ci': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Cédula de identidad'}),
            'sexo': forms.Select(attrs={'class': 'form-control dropdown m-2'}),
            'nro_telefono': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Número de telefono'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Ciudad'}),
            'nro_seguro': forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Número de seguro'}),
            'fecha_turno': forms.DateInput(attrs={'class': 'form-control m-2', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control m-2'}),
            'medico': forms.Select(attrs={'class': 'form-control dropdown m-2'}),
        }
        labels = {
            'medico' : 'Seleccione un médico',
            'ci' : 'Número de cédula',
            'nro_seguro' : 'Número de seguro',
            'nro_telefono': 'Número de telefono',
            'sexo': 'Selecione su sexo',
        }

    especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control m-2 dropdown', 'id': 'especialidad', 'placeholder': 'Seleccione una especialidad'}
        ),
        required=True

    )