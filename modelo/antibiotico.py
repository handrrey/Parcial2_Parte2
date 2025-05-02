class Antibiotico:
    def __init__(self, nombre:str, precio:float, dosis:int, tipo_animal:str):
        self.__nombre = nombre
        self.__precio = precio
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal

        if dosis < 400 or dosis > 600:
            raise ValueError("La dosis debe estar entre 400 y 600.")
        if tipo_animal not in ["bovino", "caprino", "porcino"]:
            raise ValueError("El tipo de animal debe ser 'bovino', 'caprino' o 'porcino'.")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def dosis(self):
            return self.__dosis

    @dosis.setter
    def dosis(self, dosis):
            self.__dosis = dosis

    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        self.__tipo_animal = tipo_animal
