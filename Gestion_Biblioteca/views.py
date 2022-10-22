from django.shortcuts import render, redirect
from django.template import loader
from Gestion_Biblioteca.models import *
from django.template.loader import render_to_string

from Gestion_Biblioteca.suscrip import Suscrip
from .carro import Carro
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from django.core.mail import send_mail


def Biblioteca ( request ):
    return render ( request,'Biblioteca.html' )

def Home ( request ) : 
    carro=Carro( request )
    suscrip=Suscrip(request)
    return render( request, 'home.html' )

def bibliotecas(request):  
    bibliotecas = Bibliotecas.objects.all()
    return render(request,'libros.html', {"bibliotecas":bibliotecas})
    
def revistas(request): 
    revistas = Revistas.objects.all()
    return render( request, 'revistas.html', { "revistas": revistas } )

def Iconograficos(request): 
    return render(request,'iconografico.html')

def Investigaciones_Ensayos(request):  
    return render(request,'investigaciones_ensayos.html')


def GestionBiblioteca(request):  
    return render(request,'GestionBiblioteca.html')

def RespuestaCliente(request):
    DatoCliente = request.GET['DatoCliente']
    cliente = Clientes.objects.all()
    return render(request,'Respuesta.html', {'Cliente':cliente, 'query':DatoCliente})
   
def RespuestaProveedor(request):
    DatoProveedor = request.GET['DatoProveedor']
    proveedor = Proveedores.objects.filter(Nombres__icontains = DatoProveedor)
    return render(request,'Respuesta.html',{'Proveedor':proveedor, 'query':DatoProveedor})

def RespuestaBiblioteca(request):
    DatoBiblioteca = request.GET['DatoBiblioteca']
    revista = Revistas.objects.filter(Nombre__icontains = DatoBiblioteca)
    if Bibliotecas.objects.filter(Nombre__icontains = DatoBiblioteca):
        biblioteca = Bibliotecas.objects.filter(Nombre__icontains = DatoBiblioteca)
        return render(request,'Respuesta.html',{'Biblioteca':biblioteca, 'query':DatoBiblioteca})
    else:
        return render(request,'Respuesta.html',{'Biblioteca':revista, 'query':DatoBiblioteca})
        
def RespuestaVenta(request):
    DatoVenta = request.GET['DatoVenta']
    venta = Pedido.objects.filter(id__icontains = DatoVenta)
    return render(request,'Respuesta.html', {'Venta':venta, 'query':DatoVenta})

def RespuestaSuscripcion(request):
    DatoSuscripcion = request.GET['DatoSuscripcion']
    suscripcion = Suscripcion.objects.filter(id__icontains = DatoSuscripcion)
    return render(request,'Respuesta.html', {'Suscripcion':suscripcion, 'query':DatoSuscripcion})

def Registrarse(request):
    if request.method == "POST":
        nombre=request.POST.get("NombreCliente")
        apellidos=request.POST.get("ApellidoCliente")
        edad=request.POST.get("EdadCliente")
        dni=request.POST.get("DNICliente")
        numerodni=request.POST.get("NumDNICliente")
        email=request.POST.get("EmailCliente")
        pais=request.POST.get("PaisCliente")
        ciudad=request.POST.get("CiudadCliente")
        direccion=request.POST.get("DireccionCliente")
        telefono=request.POST.get("TelefonoCliente")
        Nuevo_Cliente = Clientes(Nombres=nombre, Apellidos = apellidos, Edad = edad,
                             DNI = dni, NumeroDNI = numerodni, Email = email, Pais = pais,
                             Ciudad = ciudad, Direccion = direccion, Telefono = telefono,
                                )
        Nuevo_Cliente.save() 
        return render(request,'home.html')
    
    return render(request, "cliente.html")

def GestionVenta(request): 
    return render(request,'venta.html')

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Bibliotecas.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    messages.error(request,"Debes logearte para ingresar al carro")
    return redirect("libros")

def sumar_producto(request, producto_id):
    carro=Carro(request)
    producto=Bibliotecas.objects.get(id=producto_id)
    carro.sumar_producto(producto=producto)
    return redirect("venta")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Bibliotecas.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("venta")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Bibliotecas.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("venta")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("venta")

@login_required (login_url="autenticacion/Login")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(lineapedido(
            producto_id =key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
        
    lineapedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
    )
    
    messages.success(request,"El pedido se ha realizado satisfactoriamente")
    
    return redirect("libros")

def enviar_mail(**kwars):
    asunto="gracias por el pedido"
    mensaje= render_to_string ("pedido.html",{
        "pedido": kwars.get("pedido"),
        "lineas_pedido":kwars.get("lineas_pedido"),
        "nombreusuario":kwars.get("nombreususario")
    })
    
    mensaje_texto= strip_tags(mensaje)
    from_email="luisnic1160497@gmail.com"
    to=kwars.get("emailususario")
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
    
def GestionSuscripcion(request): 
    return render(request,'suscripcion.html')

def agregar_suscrip(request, producto_id):
    suscrip=Suscrip(request)
    producto=Revistas.objects.get(id=producto_id)
    suscrip.agregar(producto=producto)
    messages.error(request,"Debes logearte para ingresar al espacio de suscrpciones")
    return redirect("revistas")

def sumar_suscrip(request, producto_id):
    suscrip=Suscrip(request)
    producto=Revistas.objects.get(id=producto_id)
    suscrip.sumar_producto(producto=producto)
    return redirect("revistas")

def eliminar_suscrip(request, producto_id):
    suscrip=Suscrip(request)
    producto=Revistas.objects.get(id=producto_id)
    suscrip.eliminar(producto=producto)
    return redirect("revistas")

def restar_suscrip(request, producto_id):
    suscrip=Suscrip(request)
    producto=Revistas.objects.get(id=producto_id)
    suscrip.restar_producto(producto=producto)
    return redirect("revistas")

def limpiar_suscrip(request):
    suscrip=Suscrip(request)
    suscrip.limpiar_suscrip()
    return redirect("revistas")

@login_required (login_url="autenticacion/Login")
def procesar_suscrip(request):
    suscripcion=Suscripcion.objects.create(user=request.user)
    suscrip=Suscrip(request)
    lineas_suscrip=list()
    for key,value in suscrip.suscrip.items():
        lineas_suscrip.append(lineasuscripcion(
            producto_id =key,
            cantidad=value["cantidad"],
            user=request.user,
            suscripcion=suscripcion
        ))
        
    lineasuscripcion.objects.bulk_create(lineas_suscrip)
    
    enviar_mail(
        suscrip=suscrip,
        lineas_suscrip=lineas_suscrip,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
    )
    
    messages.success(request,"El pedido se ha realizado satisfactoriamente")
    
    return redirect("revistas")

def enviar_mail(**kwars):
    asunto="gracias por su suscripcion"
    mensaje= render_to_string ("suscrip.html",{
        "suscrip": kwars.get("suscrip"),
        "lineas_suscrip":kwars.get("lineas_suscrip"),
        "nombreusuario":kwars.get("nombreususario")
    })
    
    mensaje_texto= strip_tags(mensaje)
    from_email="luisnic1160497@gmail.com"
    to=kwars.get("emailususario")
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
    