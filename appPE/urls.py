from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    ## Usuario
    path('usuarios', views.UsrView.usuarios, name='usuarios'),
    path('usuario/<str:username>', views.UsrView.detalleUsuario, name='usuarioDetalle'),

    ## Ingreso
    path('ingresos', views.IngView.index, name="ingresos_index"),

    ## Gasto
    path('gastos', views.GastoView.index, name="gastos_index"),

    ## Android
    path('androidLogin', views.androidLogin, name="android_login_user"),
    path('androidCSRF', views.androidGetCSRF, name="androidCSRF"),

]