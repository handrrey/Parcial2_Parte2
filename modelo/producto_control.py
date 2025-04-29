class Producto_Control:
    def __init__(self, registro_ICA:str, nombre:str, frecuencia_aplicacion:str, precio:float):
        self.__registro_ICA = registro_ICA
        self.__nombre = nombre
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__precio = precio
        if precio < 0:
            raise ValueError("El precio debe ser positivo")

    @property
    def registro_ICA(self):
        return self.__registro_ICA

    @registro_ICA.setter
    def registro_ICA(self, registro_ICA):
        self.__registro_ICA = registro_ICA

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        self.__frecuencia_aplicacion = frecuencia_aplicacion

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio debe ser positivo")
        self.__precio = precio


    # @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)

    def asociar(self, factura):
        self.facturas = factura

    # no sabemos como va :)