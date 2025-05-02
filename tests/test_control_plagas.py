import unittest
from modelo.control_plagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):

    def setUp(self):
        self.plaga = ControlPlagas(
            registro_ICA="ICA999",
            nombre="PlagaKill",
            frecuencia_aplicacion="Mensual",
            precio=9500,
            periodo_carencia=30
        )

    def test_atributos_iniciales(self):
        self.assertEqual(self.plaga.registro_ICA, "ICA999")
        self.assertEqual(self.plaga.nombre, "PlagaKill")
        self.assertEqual(self.plaga.frecuencia_aplicacion, "Mensual")
        self.assertEqual(self.plaga.precio, 9500)
        self.assertEqual(self.plaga.periodo_carencia, 30)

    def test_setters(self):
        self.plaga.nombre = "AntiPlaga"
        self.plaga.precio = 10000
        self.plaga.periodo_carencia = 45

        self.assertEqual(self.plaga.nombre, "AntiPlaga")
        self.assertEqual(self.plaga.precio, 10000)
        self.assertEqual(self.plaga.periodo_carencia, 45)

    def test_precio_invalido(self):
        with self.assertRaises(ValueError):
            ControlPlagas("ICA002", "BugOff", "Trimestral", -10, 20)