class Factura:
    def __init__(self, cliente, fecha, productos):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__productos = productos
        self.__total = sum(producto.precio for producto in productos)

        cliente.asociar(self)

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, productos):
        self.__productos = productos

    @property
    def facturas(self):
        return self.__facturas

    @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)

    def asociar(self, factura):
        self.facturas = factura
