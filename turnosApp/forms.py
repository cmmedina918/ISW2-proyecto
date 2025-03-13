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
        exclude = ['fecha_registro', 'id']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del paciente'}),
            'ci': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula de identidad'}),
            'nro_seguro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de seguro'}),
            'fecha_turno': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'medico': forms.Select(attrs={'class': 'dropdown'}),
        }
        labels = {
            'medico' : 'Seleccione un médico',
            'ci' : 'Número de cédula',
            'nro_seguro' : 'Número de seguro',
        }