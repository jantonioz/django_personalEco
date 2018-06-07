from django.contrib import admin
from .models import Usuario, Ingreso, Gasto
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ingreso)
admin.site.register(Gasto)