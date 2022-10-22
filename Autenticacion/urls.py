from django.urls import path
from .views import V_Registro, Cerrar_Sesion,Login


urlpatterns = [
   path('',V_Registro.as_view(), name='Autenticacion'),
   path('Cerrar_Sesion',Cerrar_Sesion, name='Cerrar_Sesion'),
   path('Login',Login, name='Login'),
]
