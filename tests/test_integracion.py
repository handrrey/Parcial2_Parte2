import unittest
from crud import cliente_crud, producto_crud
from modelo.factura import Factura
from modelo.antibiotico import Antibiotico

class TestIntegracionPrograma(unittest.TestCase):

    def setUp(self):
        # Limpiar todos los registros antes de cada test
        cliente_crud.clientes_registrados.clear()

    def test_flujo_completo_registro_venta_factura(self):
        # Paso 1: Registrar un cliente
        cliente = cliente_crud.registrar_cliente("Pedro Salazar", "55555")
        self.assertIn("55555", cliente_crud.clientes_registrados)

        # Paso 2: Venderle un producto (antibiótico)
        producto_crud.vender_producto("55555", "antibiotico", 1, "2025-05-01", 17000)

        # Paso 3: Validar que el cliente tiene una factura creada
        self.assertEqual(len(cliente.facturas), 1)
        factura = cliente.facturas[0]
        self.assertIsInstance(factura, Factura)

        # Paso 4: Validar que la factura tiene el producto correcto
        producto_vendido = factura._Factura__productos[0]
        self.assertIsInstance(producto_vendido, Antibiotico)
        self.assertEqual(producto_vendido.nombre, producto_crud.antibioticos_disponibles[0].nombre)
        self.assertEqual(producto_vendido.precio, 17000)

        # Paso 5: Validar los datos de la factura
        self.assertEqual(factura._Factura__fecha, "2025-05-01")
        self.assertEqual(factura._Factura__total, 17000)

    def test_cliente_no_factura_si_producto_invalido(self):
        # Registrar cliente
        cliente = cliente_crud.registrar_cliente("Maria Lopez", "66666")

        # Intentar vender producto con selección inválida
        producto_crud.vender_producto("66666", "fertilizante", 999, "2025-05-01", 20000)

        # Verificar que NO tiene facturas
        self.assertEqual(len(cliente.facturas), 0)

    def test_no_se_puede_vender_a_cliente_inexistente(self):
        # Intentar vender a cédula inexistente
        producto_crud.vender_producto("77777", "control_plagas", 1, "2025-05-01", 21000)

        # Confirmar que no se creó cliente por accidente
        self.assertNotIn("77777", cliente_crud.clientes_registrados)


if __name__ == "__main__":
    unittest.main()
