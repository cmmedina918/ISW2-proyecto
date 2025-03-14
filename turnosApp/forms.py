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
        exclude = ['fecha_registro', 'id','status']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control m-1', 'placeholder': 'Nombre del paciente'}),
            'ci': forms.TextInput(attrs={'class': 'form-control m-1', 'placeholder': 'Cédula de identidad'}),
            'sexo': forms.Select(attrs={'class': 'form-control dropdown m-1'}),
            'nro_telefono': forms.TextInput(attrs={'class': 'form-control m-1', 'placeholder': 'Número de telefono'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control m-1', 'placeholder': 'Ciudad'}),
            'nro_seguro': forms.TextInput(attrs={'class': 'form-control m-1', 'placeholder': 'Número de seguro'}),
            'fecha_turno': forms.DateInput(attrs={'class': 'form-control m-1', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control m-1'}),
            'medico': forms.Select(attrs={'class': 'form-control dropdown m-1'}),
        }
        labels = {
            'medico' : 'Seleccione un médico',
            'ci' : 'Número de cédula',
            'nro_seguro' : 'Número de seguro',
            'nro_telefono': 'Número de telefono',
            'sexo': 'Selecione su sexo'
        }