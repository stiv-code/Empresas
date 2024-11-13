from django.db import models

# Create your models here.
class Candidatos(models.Model):
    id_can = models.CharField(max_length=10, blank=True, property=True)
    nombre_can = models.CharField(max_length=100, blank=True)
    apellido_can = models.CharField(max_length=100, blank=True)
    email_can = models.(max_length=100, blank=True)
    telefono_can = models.CharField(max_length=10, blank=True)
    fecha_nac_can = models.DateField(blank=True)
    genero_can = models.CharField(max_length=1)
    titulo_can = models.CharField(max_length=50, blank=True)

    def __str__(self):
         return self.nombre_can

class Vacantes(models.Model):
    id_vac = models.CharField(max_length=10,blank=True, property=True)
    nom_vac = models.CharField(max_length=30, blank=False)
    id_can = models.ForeignKey(Vacantes, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom_vac

class locales(models.Model):
    id_loc = models.CharField(max_length=10, blank=True, property=True)
    nombre_loc = models.CharField(max_length=50, blank=False)
    direccion_loc = models.CharField(max_length=100, blank=False)
    id_vac = models.ForeignKey(Vacantes, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre_loc

class contrato(models.Model):
    id_con = models.CharField(max_length=10, blank=True, property=True)
    fecha_ini_con = models.DateField(blank=False)
    fecha_fin_con = models.DateField(blank=False)
    salario = models.CharField()
    id_loc = models.ForeignKey(locales, on_delete=models.RESTRICT)
    id_can = models.ForeignKey(Vacantes, on_delete=models.RESTRICT)
    id_emp = models.ForeignKey('Empleados', on_delete=models.RESTRICT)

    def __str__(self):
        return self.id_con