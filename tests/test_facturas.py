import unittest

from modelo.control_plagas import ControlPlagas
from modelo.factura import Factura
from modelo.cliente import Cliente
from modelo.antibiotico import Antibiotico
from modelo.fertilizante import Fertilizante
from modelo.producto_control import Producto_Control


class TestFactura(unittest.TestCase):
    def test_factura_creacion_y_total(self):

        cliente = Cliente("Luis Perez", "16136690")

        antibiotico1 = Antibiotico("Penicilina", 50000, 500, "bovino")
        fertilizante1 = Fertilizante("ICA0", "Urea", "30 días", 25000, "01/02/2025")
        controlPlagas1 = ControlPlagas("ICA1", "Veneno", "15 dias", 15000, "150 dias" )


        productos = [antibiotico1, fertilizante1, controlPlagas1]
        factura = Factura(cliente, "17/04/2025", productos)

        self.assertEqual(factura._Factura__total, 90000)

        self.assertIn(factura, cliente.facturas)

        self.assertEqual(len(factura._Factura__productos), 3)

        self.assertEqual(factura._Factura__productos[0].nombre, "Penicilina")
        self.assertEqual(factura._Factura__productos[1].nombre, "Urea")
        self.assertEqual(factura._Factura__productos[2].nombre, "Veneno")

if __name__ == '__main__':
    unittest.main()
