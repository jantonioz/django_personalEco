from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def economia(self):
        ingresos = Ingreso.objects.filter(usuario=self)
        gastos = Gasto.objects.filter(usuario=self)
        suma_i = suma_g = 0
        for ingreso in ingresos:
            suma_i += ingreso.total
        for gasto in gastos:
            suma_g += gasto.total

        return suma_i - suma_g

    def totalGastos(self):
        gastos = Gasto.objects.filter(usuario=self)
        suma = 0
        for gasto in gastos:
            suma += gasto.total
        return suma
    
    def totalIngresos(self):
        ingresos = Ingreso.objects.filter(usuario=self)
        suma = 0
        for i in ingresos:
            suma += i.total
        return suma

class Ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None, blank=True)
    total = models.FloatField()
    descripcion = models.CharField(max_length=160)
    fecha_hora = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Gasto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None, blank=True)
    total = models.FloatField()
    descripcion = models.CharField(max_length=160)
    fecha_hora = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)