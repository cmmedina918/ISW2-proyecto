from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

# Create your models here.
class Especialidad(models.Model):

    nombre = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return self.nombre

class Medico(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nro_matricula = models.CharField(max_length=50, null=False, unique=True)
    nro_cedula = models.CharField(max_length=20, null=False, default="0000", unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    especialidades = models.ManyToManyField('Especialidad', blank=True) # Ajusta si es necesario

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Sexo(models.Model):

    nombre = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):

    nombre = models.CharField(max_length=100, null=False)
    ci = models.CharField(max_length=20, null=False)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    conacto = models.CharField(max_length=100, null=False)
    tipo_contacto = models.BooleanField(default=False, null=False)
    ciudad = models.CharField(max_length=50, null=True)
    status = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.ci

class Turno(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(default=now, null=False)
    fecha_turno = models.DateField( null=False)
    status = models.IntegerField(null=False, default=0)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True)

    def __str__(self):
        return self.paciente.nombre

