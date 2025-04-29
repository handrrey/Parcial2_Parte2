import unittest
from modelo.fertilizante import Fertilizante

class TestFertilizante(unittest.TestCase):

    def setUp(self):
        self.fertilizante = Fertilizante(
            registro_ICA="ICA123",
            nombre="FertiPlus",
            frecuencia_aplicacion="Cada 15 días",
            precio=12000,
            ultima_apliacion="2025-04-01"
        )

    def test_atributos_iniciales(self):
        self.assertEqual(self.fertilizante.registro_ICA, "ICA123")
        self.assertEqual(self.fertilizante.nombre, "FertiPlus")
        self.assertEqual(self.fertilizante.frecuencia_aplicacion, "Cada 15 días")
        self.assertEqual(self.fertilizante.precio, 12000)
        self.assertEqual(self.fertilizante.ultima_aplicacion, "2025-04-01")

    def test_setters(self):
        self.fertilizante.nombre = "SuperFerti"
        self.fertilizante.precio = 15000
        self.fertilizante.ultima_aplicacion = "2025-04-15"

        self.assertEqual(self.fertilizante.nombre, "SuperFerti")
        self.assertEqual(self.fertilizante.precio, 15000)
        self.assertEqual(self.fertilizante.ultima_aplicacion, "2025-04-15")

    def test_precio_invalido(self):
        with self.assertRaises(ValueError):
            Fertilizante("ICA456", "EcoFert", "Semanal", -100, "2025-04-01")