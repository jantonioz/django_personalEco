from django.urls import path

from . import views

urlpatterns = [
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuario/<str:username>', views.detalleUsuario, name='usuarioDetalle'),

]