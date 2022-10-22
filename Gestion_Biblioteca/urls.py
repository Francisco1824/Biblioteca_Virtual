from . import views
from django.urls import path

app_name = 'carro'

urlpatterns = [
        path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
        path('sumar/<int:producto_id>/', views.sumar_producto, name="sumar"),
        path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"), 
        path('restar/<int:producto_id>/', views.restar_producto, name="restar"), 
        path('limpiar/', views.limpiar_carro, name="limpiar"),
        
        path('agregarsuscrip/<int:producto_id>/', views.agregar_suscrip, name="agregarsuscrip"),
        path('sumarsuscrip/<int:producto_id>/', views.sumar_suscrip, name="sumarsuscrip"),
        path('eliminarsuscrip/<int:producto_id>/', views.eliminar_suscrip, name="eliminarsuscrip"), 
        path('restarsuscrip/<int:producto_id>/', views.restar_suscrip, name="restarsuscrip"), 
        path('limpiarsuscrip/', views.limpiar_suscrip, name="limpiarsuscrip"), 
    ]