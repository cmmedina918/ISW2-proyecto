from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Medico)
admin.site.register(Especialidad)
admin.site.register(Turno)
# admin.site.register(Sexo)
admin.site.register(Paciente)