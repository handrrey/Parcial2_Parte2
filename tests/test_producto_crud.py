import unittest
from unittest.mock import patch
from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico
from crud.producto_crud import vender_productos, obtener_producto, clientes_registrados, antibioticos_disponibles, fertilizantes_disponibles, productos_control_plagas_disponibles, facturas_registradas

class TestProductoCRUD(unittest.TestCase):

    def setUp(self):
        clientes_registrados.clear()
        facturas_registradas.clear()

    def test_obtener_producto_antibiotico_invalido(self):
        producto = obtener_producto("antibiotico", 100)
        self.assertIsNone(producto)

    def test_obtener_producto_fertilizante_valido(self):
        producto = obtener_producto("fertilizante", 2)
        self.assertIsInstance(producto, Fertilizante)
        self.assertEqual(producto.nombre, "SuperGrow")

    def test_obtener_producto_fertilizante_invalido(self):
        producto = obtener_producto("fertilizante", 0)
        self.assertIsNone(producto)

    def test_obtener_producto_control_plagas_valido(self):
        producto = obtener_producto("control plagas", 3)
        self.assertIsInstance(producto, ControlPlagas)
        self.assertEqual(producto.nombre, "PlagaStop")

    def test_obtener_producto_control_plagas_invalido(self):
        producto = obtener_producto("control plagas", 6)
        self.assertIsNone(producto)

    def test_obtener_producto_tipo_invalido(self):
        producto = obtener_producto("otro_tipo", 1)
        self.assertIsNone(producto)

if __name__ == '__main__':
    unittest.main()