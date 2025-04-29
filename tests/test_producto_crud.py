import unittest
from crud import producto_crud
from crud import cliente_crud
from modelo.factura import Factura


class TestProductoCRUD(unittest.TestCase):

    def setUp(self):
        # Limpiamos clientes antes de cada test
        cliente_crud.clientes_registrados.clear()

    def test_vender_producto_exitoso(self):
        cliente = cliente_crud.registrar_cliente("Luis Martínez", "22222")
        producto_crud.vender_producto("22222", "antibiotico", 1, "2025-04-28", 16000)

        # Verificar que el cliente tiene una factura asociada
        self.assertEqual(len(cliente.facturas), 1)
        factura = cliente.facturas[0]
        self.assertIsInstance(factura, Factura)
        self.assertEqual(factura._Factura__productos[0].nombre, producto_crud.antibioticos_disponibles[0].nombre)

    def test_vender_producto_cliente_no_registrado(self):
        # Intentar vender a un cliente no registrado
        producto_crud.vender_producto("33333", "fertilizante", 1, "2025-04-28", 18000)
        # Asegurarse que el cliente sigue sin existir en la base
        self.assertNotIn("33333", cliente_crud.clientes_registrados)

    def test_vender_producto_seleccion_invalida(self):
        cliente = cliente_crud.registrar_cliente("Laura González", "44444")
        producto_crud.vender_producto("44444", "antibiotico", 99, "2025-04-28", 15000)  # Selección inválida
        # Asegurarse que no se creó ninguna factura
        self.assertEqual(len(cliente.facturas), 0)


if __name__ == "__main__":
    unittest.main()

