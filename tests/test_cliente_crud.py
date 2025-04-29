import unittest
from crud import cliente_crud
from modelo.cliente import Cliente

class TestClienteCRUD(unittest.TestCase):

    def setUp(self):

        cliente_crud.clientes_registrados.clear()

    def test_registrar_cliente_nuevo(self):
        cliente = cliente_crud.registrar_cliente("Juan Pérez", "12345")
        self.assertIsInstance(cliente, Cliente)
        self.assertIn("12345", cliente_crud.clientes_registrados)
        self.assertEqual(cliente_crud.clientes_registrados["12345"].nombre, "Juan Pérez")

    def test_registrar_cliente_duplicado(self):
        cliente_crud.registrar_cliente("Ana Gómez", "67890")
        cliente_existente = cliente_crud.registrar_cliente("Ana Gómez", "67890")
        # Verificar que no se crea un nuevo cliente
        self.assertEqual(len(cliente_crud.clientes_registrados), 1)
        self.assertEqual(cliente_existente.nombre, "Ana Gómez")

    def test_buscar_cliente_existente(self):
        cliente = cliente_crud.registrar_cliente("Carlos Ruiz", "11111")
        # Simular búsqueda simplemente accediendo
        cliente_buscado = cliente_crud.clientes_registrados.get("11111")
        self.assertIsNotNone(cliente_buscado)
        self.assertEqual(cliente_buscado.nombre, "Carlos Ruiz")

    def test_buscar_cliente_inexistente(self):
        cliente_buscado = cliente_crud.clientes_registrados.get("99999")
        self.assertIsNone(cliente_buscado)

if __name__ == "__main__":
    unittest.main()