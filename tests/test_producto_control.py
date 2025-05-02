import unittest
from modelo.producto_control import Producto_Control

class TestProductoControl(unittest.TestCase):

    def test_creacion_valida(self):
        producto = Producto_Control("ICA3", "MataRatas", "Cada 20 días", 60000)
        self.assertEqual(producto.registro_ICA, "ICA3")
        self.assertEqual(producto.nombre, "MataRatas")
        self.assertEqual(producto.frecuencia_aplicacion, "Cada 20 días")
        self.assertEqual(producto.precio, 60000)

    def test_precio_valido(self):
        with self.assertRaises(ValueError):
            Producto_Control("ICA4", "Fungicida", "Cada 10 días", -5000)

if __name__ == '__main__':
    unittest.main()
