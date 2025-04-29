import unittest
from modelo.cliente import Cliente

class TestCliente(unittest.TestCase):

    def test_creacion_valida(self):
        cliente = Cliente("Luis", "16136690")
        self.assertEqual(cliente.nombre, "Luis")
        self.assertEqual(cliente.cedula, "16136690")

    def test_nombre_valido(self):
        with self.assertRaises(ValueError):
            Cliente("852", "16136690") #Nombre que no es una cadena

    def test_cedula_valido(self):
        with self.assertRaises(ValueError):
            Cliente("Luis", "abdc") #Cedula que no es una cadena numerica
            Cliente("Luis", 1234)


if __name__ == "__main__":
    unittest.main()