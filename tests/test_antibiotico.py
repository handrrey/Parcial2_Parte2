import unittest
from modelo.antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):

    def test_creacion_valida(self):
        antibiotico = Antibiotico("Penicilina", 50000, 450, "bovino")
        self.assertEqual(antibiotico.nombre, "Penicilina")
        self.assertEqual(antibiotico.precio, 50000)
        self.assertEqual(antibiotico.dosis, 450)
        self.assertEqual(antibiotico.tipo_animal, "bovino")

    def test_dosis_invalida(self):
        with self.assertRaises(ValueError):
            Antibiotico("Penicilina", 50000, 300, "bovino")  # Dosis fuera de rango

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            Antibiotico("Penicilina", 50000, 450, "gato")  # Tipo animal inválido

if __name__ == "__main__":
    unittest.main()
