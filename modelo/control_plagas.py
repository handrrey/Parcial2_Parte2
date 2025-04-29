from modelo.producto_control import Producto_Control

class ControlPlagas (Producto_Control):
    def __init__(self, registro_ICA:str, nombre:str, frecuencia_aplicacion:str, precio:float, periodo_carencia:int):
        super().__init__(registro_ICA, nombre, frecuencia_aplicacion, precio)
        self.__periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia

