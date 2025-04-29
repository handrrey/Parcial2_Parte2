from modelo.producto_control import Producto_Control

class Fertilizante (Producto_Control):
    def __init__(self, registro_ICA:str, nombre:str, frecuencia_aplicacion:str, precio:float, ultima_apliacion:str):
        super().__init__( registro_ICA, nombre, frecuencia_aplicacion, precio)
        self.__ultima_aplicacion = ultima_apliacion

    @property
    def ultima_aplicacion(self):
        return self.__ultima_aplicacion

    @ultima_aplicacion.setter
    def ultima_aplicacion(self, ultima_aplicacion):
        self.__ultima_aplicacion = ultima_aplicacion
