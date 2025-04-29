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

def buscar_por_cedula(cedula: str):
    cliente = clientes_registrados.get(cedula)
    if not cliente:
        print("Cliente no encontrado.")
        return
    print(f"\nCliente: {cliente.nombre} - Cédula: {cliente.cedula}")
    print(f"Facturas ({len(cliente.facturas)}):")
    for i, factura in enumerate(cliente.facturas, start=1):
        print(f"\nFactura {i} - Fecha: {factura._Factura__fecha}")
        for prod in factura._Factura__productos:
            print(f"Producto: {prod.nombre}")
            print(f"  Precio: ${prod.precio}")
            if hasattr(prod, 'dosis'):
                print(f"  Dosis: {prod.dosis}mg")
                print(f"  Tipo de Animal: {prod.tipo_animal}")
            if hasattr(prod, 'registro_ICA'):
                print(f"  Registro ICA: {prod.registro_ICA}")
                print(f"  Frecuencia de Aplicación: {prod.frecuencia_aplicacion}")
                if hasattr(prod, 'periodo_carencia'):
                    print(f"  Periodo de Carencia: {prod.periodo_carencia} días")
                if hasattr(prod, 'ultima_aplicacion'):
                    print(f"  Última Aplicación: {prod.ultima_aplicacion}")