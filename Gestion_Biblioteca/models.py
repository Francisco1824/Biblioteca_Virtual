from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField

User=get_user_model()

class Clientes(models.Model): #crear tabla Clientes,solcitando los siguientes datos
    id= models.AutoField(primary_key = True)    
    Nombres = models.CharField(max_length = 70)
    Apellidos = models.CharField(max_length = 70)
    Edad = models.SmallIntegerField(default = "18")
    DNI = models.CharField(max_length = 20, default = "Cedula")
    NumeroDNI = models.BigIntegerField()
    Email = models.EmailField()
    Pais = models.CharField(max_length = 50)
    Ciudad = models.CharField(max_length = 50)
    Direccion = models.CharField(max_length = 70)
    Telefono = models.BigIntegerField()
    Fecha_Registro= models.DateField(auto_now_add = True)
        
    def __str__(self):  #retorno de como sera mostrado al crear el cliente
    
        return ("Nombre completo: %s %s" % (self.Apellidos, self.Nombres))


class Proveedores(models.Model):    #crear tabla Priveedores,solcitando los siguientes datos
    idProveedor = models.AutoField(primary_key = True)
    Nombres = models.CharField(max_length = 70)
    NIT = models.BigIntegerField()
    Email = models.EmailField()
    Direccion = models.CharField(max_length = 70)
    Telefono = models.BigIntegerField()
    
    def DatosProveedor(self):
        cadena = "Nombre Proveedor: {0}\n Email: {1}\n Telefono: {2}"
        return cadena.format(self.Nombres, self.Email, self.Telefono)

    def __str__(self):  #retorno de como sera mostrado al crear el Proveedor
        return self.DatosProveedor()

class Bibliotecas(models.Model):    #crear tabla Biblioteca,solcitando los siguientes datos, llevra una llave foranea de proveedores
    id = models.AutoField(primary_key = True)
    Nombre = models.CharField(max_length = 100)
    Imagen = models.URLField( max_length = 200)
    Autor = models.CharField(max_length = 150)
    Tipo = models.CharField(max_length = 50)
    Genero = models.CharField(max_length = 35 )
    Resumen = models.CharField(max_length = 2000)
    FechaPublicacion = models.DateField()
    Nacionalidad = models.CharField(max_length = 50)
    Proveedor = models.ForeignKey(Proveedores, on_delete = models.CASCADE) 
    Estado = models.BooleanField(default = True)
    PrecioNeto = models.FloatField()
    PrecioVenta = models.FloatField()
    PrecioSuscripcion = models.FloatField()

      
    def ServVenta(self):    #Defino el servicio de compra
        cadena = "Servicio de compra => {0}, {1} {2}"
        return cadena.format(self.PrecioVenta, self.Tipo, self.Nombre)

    def ServSuscripcion(self): #Defino el servicio de alquiler
        cadena = "Servicio de alquiler => {0}, {1} {2}"
        return cadena.format(self.PrecioSuscripcion, self.Tipo, self.Nombre)
    

    def __str__ (self):     #datos que se mostraran al crear el producto
        
        return self.Nombre
        
    def FichaTecnica(self):
        cadena = "{0} {1} \n Autor: {2} \n {3}"
        return cadena.format(self.Tipo, self.Nombre, self.Autor, self.Resumen)
    
    
class Revistas(models.Model): 
    id = models.AutoField(primary_key = True)
    Nombre = models.CharField(max_length = 100)
    Imagen = models.URLField( max_length = 200)
    Autor = models.CharField(max_length = 150)
    Tipo = models.CharField(max_length = 50)
    Genero = models.CharField(max_length = 35 )
    Resumen = models.CharField(max_length = 2000)
    FechaPublicacion = models.DateField()
    Nacionalidad = models.CharField(max_length = 50)
    Proveedor = models.ForeignKey(Proveedores, on_delete = models.CASCADE) 
    Estado = models.BooleanField(default = True)
    PrecioNeto = models.FloatField()
    PrecioVenta = models.FloatField()
    PrecioSuscripcion = models.FloatField()
    
    def __str__ (self):     #datos que se mostraran al crear el producto
        
        return self.Nombre
    

class Pedido(models.Model):     #crear tabla Ventas,solcitando los siguientes datos,llevara llaves foraneas de cliente y biblioteca
    user = models.ForeignKey(User, on_delete = models.CASCADE, default ="")    
    created_at = models.DateField(auto_now_add = True)
    

    def __str__(self): 
       return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('precio')*F('cantidad'), output_field=FloatField())
        )["total"]
    
    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']
        
class lineapedido(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    producto = models.ForeignKey(Bibliotecas, on_delete = models.CASCADE)
    pedido = models.ForeignKey(Pedido, null=True, on_delete = models.SET_NULL)
    cantidad=models.IntegerField(default='1')
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self): 
       return f'{self.cantidad} unidades de {self.producto_id.Nombre}'
    
    class Meta:
        db_table='lineapedidos'
        verbose_name='Lineapedido'
        verbose_name_plural='Lineapedidos'
        ordering=['id']
    
class Suscripcion(models.Model):     #crear tabla Ventas,solcitando los siguientes datos,llevara llaves foraneas de cliente y biblioteca
    user = models.ForeignKey(User, on_delete = models.CASCADE)    
    created_at = models.DateField(auto_now_add = True)
    

    def __str__(self): 
       return self.id
    
    @property
    def total(self):
        return self.lineasuscripcion_set.aggregate(
            total=Sum(F('precio')*F('cantidad'), output_field=FloatField())
        )["total"]
    
    class Meta:
        db_table='suscripciones'
        verbose_name='suscripcion'
        verbose_name_plural='suscripciones'
        ordering=['id']
        
class lineasuscripcion(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    producto = models.ForeignKey(Revistas, null=True, on_delete = models.CASCADE)
    suscripcion = models.ForeignKey(Suscripcion, null=True, on_delete = models.SET_NULL)
    cantidad=models.IntegerField(default='1')
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self): 
       return f'{self.cantidad} unidades de {self.suscripcion_id}'
    
    class Meta:
        db_table='lineasuscripciones'
        verbose_name='lineasuscripcion'
        verbose_name_plural='lineasuscripciones'
        ordering=['id']
    
