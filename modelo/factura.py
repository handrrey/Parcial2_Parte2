class Factura:
    def __init__(self, cliente, fecha, productos):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__productos = productos
        self.__total = sum(producto.precio for producto in productos)

        cliente.asociar(self)

    @property
    def facturas(self):
        return self.__facturas

    @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)

    def asociar(self, factura):
        self.facturas = factura
