from modelo.cliente import Cliente
from modelo.factura import Factura

# Simulación de base de datos en memoria
clientes_registrados = {}

def registrar_cliente(nombre: str, cedula: str):
    if cedula in clientes_registrados:
        print("Cliente ya registrado.")
        return clientes_registrados[cedula]
    cliente = Cliente(nombre, cedula)
    clientes_registrados[cedula] = cliente
    print(f"Cliente {nombre} registrado correctamente.")
    return cliente

def buscar_cliente_por_cedula(cedula: str):
    return clientes_registrados.get(cedula)

def mostrar_info_cliente(cliente):
    print(f"\nCliente: {cliente.nombre} - Cédula: {cliente.cedula}")
    print(f"Facturas ({len(cliente.facturas)}):")

    for i, factura in enumerate(cliente.facturas, start=1):
        print(f"\nFactura {i} - Fecha: {factura.fecha} ")
        for prod in factura.productos:
            print(f"Producto: {prod.nombre}")
            print(f"  Precio: ${prod.precio}")


def buscar_por_cedula(cedula: str):
    cliente = buscar_cliente_por_cedula(cedula)
    if cliente is None:
        raise ValueError("Cliente no encontrado.")
    else:
        mostrar_info_cliente(cliente)
