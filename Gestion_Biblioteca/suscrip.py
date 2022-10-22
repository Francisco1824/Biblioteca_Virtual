class Suscrip:
    def __init__( self , request ) :
        self.request = request
        self.session = request.session
        suscrip = self.session.get( "suscrip" )
        if not suscrip:
            suscrip = self.session["suscrip"] = {}
        #else:
        self.suscrip = suscrip

    def guardar_suscrip ( self ) :
        self.session["suscrip"] = self.suscrip
        self.session.modified = True

    def agregar ( self,producto ) :
        if str ( producto.id not in self.suscrip.keys ( ) ):
            self.suscrip[producto.id] = {
                "producto_id":producto.id,
                "nombre": producto.Nombre,
                "precio": str ( producto.PrecioSuscripcion ),
                "cantidad": 1,
                "imagen": producto.Imagen.url
            }       
        else:
            for key, value in self.suscrip.items ():
                if  key == str ( producto.id ) :
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.guardar_suscrip()

    def sumar_producto ( self,producto ) :
        for key, value in self.suscrip.items () :
                if  key == str ( producto.id ):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float( value["precio"] ) + producto.PrecioSuscripcion
                    break
        self.guardar_suscrip()
    
    def total_suscrip ( self,producto ) :
        for key, value in self.suscrip.items():
                if  key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.PrecioSuscripcion 
                    break
        self.guardar_suscrip()
            
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.suscrip:
            del self.suscrip[producto.id]
            self.guardar_suscrip()

    def restar_producto(self, producto):
        for key, value in self.suscrip.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - producto.PrecioSuscripcion 
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_suscrip()

    def limpiar_suscrip(self):
        self.session["suscrip"] = {}
        self.session.modified = True
        