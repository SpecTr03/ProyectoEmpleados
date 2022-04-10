from distutils.command.upload import upload
from django.db import models
from applications.departamento.models import DepartamentoModelo
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidad Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    #Modelo para la tabla empleado
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120,blank=True)
    job = models.CharField('Trabajo',max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(DepartamentoModelo, on_delete=models.CASCADE)
    #para una relacion de muchos a muchos
    habilidades = models.ManyToManyField(Habilidades)
    avatar = models.ImageField(upload_to='empleado',blank=True,null=True)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
