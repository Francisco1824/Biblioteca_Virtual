"""Biblioteca_Virtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from Gestion_Biblioteca.views import *
from Biblioteca_Virtual import settings
from django.conf.urls.static import static
from Biblioteca_Virtual.settings import MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include('Autenticacion.urls')),
    path('',Home, name="home"),
    path('Registrarse/',Registrarse, name = "registrarse"),
    path('libros/',bibliotecas, name="libros"),
    path('venta/',GestionVenta, name= "venta"),
    path('suscripcion/',GestionSuscripcion, name= "suscripcion"),
    path('carro/',include('Gestion_Biblioteca.urls')),
    path('revistas/',revistas, name= "revistas"),
    path('iconograficos/',Iconograficos, name="iconograficos"),
    path('investigaciones_ensayos/',Investigaciones_Ensayos, name="inv_ens"),
    #path('gestionbiblioteca/',GestionBiblioteca),
    #path('DatoCliente/',RespuestaCliente),
    #path('DatoProveedor/',RespuestaProveedor),
    path('DatoBiblioteca/',RespuestaBiblioteca),
    #path('DatoVenta/',RespuestaVenta),
    #path('DatoSuscripcion/',RespuestaSuscripcion),
    path('pedido/',procesar_pedido, name='procesar_pedido'),
    path('suscrip/',procesar_suscrip, name='procesar_suscrip'),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

