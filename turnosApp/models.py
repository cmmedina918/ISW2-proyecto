from django.db import models
from django.utils.timezone import now

# Create your models here.
class Especialidades(models.Model):

    nombre = models.CharField(max_length= 100, null= False)

    def __srt__(self):
        return self.nombre

class Medicos(models.Model):
    nombre = models.CharField(max_length= 100, null=False )
    nro_matricula = models.CharField(max_length= 50, null=False )
    telefono = models.CharField(max_length=20)
    especialidades = models.ManyToManyField(Especialidades, blank=True)

    def __srt__(self):
        return self.nombre

class Turnos(models.Model):
    fecha_registro = models.DateTimeField(default=now, null=False)
    fecha_turno = models.DateField( null=False)
    nombre = models.CharField(max_length=100, null=False)
    ci = models.CharField(max_length=20, null=False)
    nro_seguro = models.CharField(max_length=20, null=False)
    medico = models.OneToOneField(Medicos, on_delete=models.CASCADE, primary_key=True)

    def __srt__(self):
        return self.fecha_turno