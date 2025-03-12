from django import forms
from .models import *

class especialidadesForm(forms.ModelForm):
    class Meta:
        model = Especialidades
        fields = ['Nombre: ']

class medicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['Nombre: ', 'Número de matriula:', 'Telefono: ']

class turnoForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['Nombre:', 'Numero de Cedula:', 'Numero de Seguro:', 'Fecha de Consulta:']