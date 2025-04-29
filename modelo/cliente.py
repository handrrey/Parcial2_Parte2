class Cliente:

    def __init__(self, nombre: str, cedula: str):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = []

        if not isinstance(nombre, str) or nombre.isdigit():
            raise ValueError("El nombre no tiene el tipo de dato correcto.")

        if not isinstance(cedula, str) or not cedula.isdigit():
            raise ValueError("La cédula debe ser una cadena numérica.")

    @property
    def facturas(self):
        return self.__facturas

    @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)

    def asociar(self, factura):
        self.facturas = factura

    # Este método ya no es necesario si solo usas 'asociar'
    # def agregar_factura(self, factura):
    #     self.__facturas.append(factura)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula