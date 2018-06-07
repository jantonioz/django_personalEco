from django.shortcuts import render
from .models import Usuario, Ingreso, Gasto

# Create your views here.
def usuarios(request):
    return render(request, 'Usuario/usuarios.html', 
    {'usuarios': Usuario.objects.all()})

def detalleUsuario(request, username):
    u = Usuario.objects.get(username=username)
    ingresos = u.ingreso_set.all()
    gastos = u.gasto_set.all()
    return render(request, 'Usuario/detalle.html', 
    {'usuario': u, 'ingresos' : ingresos, 'gastos': gastos})