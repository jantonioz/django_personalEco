from django.shortcuts import render, HttpResponse
from .models import Usuario, Ingreso, Gasto
from django.views.decorators.csrf import csrf_exempt



def androidGetCSRF(request):
    return render(request, 'Android/csrf.html')


@csrf_exempt
def androidLogin(request):
    if request.method == 'POST':
        usr = request.POST.get('usr')
        pwd = request.POST.get('pass')

        try:
            u = Usuario.objects.get(username=usr, password = pwd)
            return HttpResponse( u.nombre, content_type="text/plain; charset=utf-8")
        except Exception:
            return HttpResponse(pwd, content_type="text/plain")
    return HttpResponse( "", content_type="text/plain")



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