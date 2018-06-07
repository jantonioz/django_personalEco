from django.shortcuts import render
from .models import Usuario, Ingreso, Gasto

# Create your views here.
def index(request):
    top3_usrs = sorted(Usuario.objects.all(), key=lambda a : a.economia())[::-1]
    top3_usrs = top3_usrs[:3]
    return render(request, 'index.html', {'usuarios': top3_usrs})

class GastoView():
    def index(request):
        g = Gasto.objects.all()
        return render(request, 'Gasto/gastos.html', {'gastos': g})

class IngView():
    def index(request):
        igs = Ingreso.objects.all()
        return render(request, 'Ingreso/ingresos.html', {'ingresos': igs})

class UsrView():
    def usuarios(request):
        return render(request, 'Usuario/usuarios.html', 
        {'usuarios': Usuario.objects.all()})

    def detalleUsuario(request, username):
        u = Usuario.objects.get(username=username)
        ingresos = u.ingreso_set.all()
        gastos = u.gasto_set.all()
        return render(request, 'Usuario/detalle.html', 
        {'usuario': u, 'ingresos' : ingresos, 'gastos': gastos})