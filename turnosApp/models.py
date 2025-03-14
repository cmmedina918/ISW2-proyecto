from django.db import models
from django.utils.timezone import now

# Create your models here.
class Especialidad(models.Model):

    nombre = models.CharField(max_length= 100, null= False)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length= 100, null=False )
    nro_matricula = models.CharField(max_length= 50, null=False )
    telefono = models.CharField(max_length=20)
    especialidades = models.ManyToManyField(Especialidad, blank=True)

    def __str__(self):
        return self.nombre

class Sexo(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ci = models.CharField(max_length=20, null=False)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    nro_seguro = models.CharField(max_length=20, null=False)
    nro_telefono = models.CharField(max_length=20, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    fecha_registro = models.DateTimeField(default=now, null=False)
    fecha_turno = models.DateField( null=False)
    status = models.IntegerField(null=False, default=0)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre