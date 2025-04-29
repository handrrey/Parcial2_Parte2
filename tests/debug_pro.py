from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.antibiotico import Antibiotico
from modelo.producto_control import Producto_Control
from modelo.fertilizante import Fertilizante
from modelo.control_plagas import ControlPlagas


def main():

    cliente = Cliente(nombre="Juan Pérez", cedula="1234567890")

    antibiotico1 = Antibiotico(nombre="AmoxiVet", precio=15000, dosis=500, tipo_animal="bovino")
    antibiotico2 = Antibiotico(nombre="PorciPen", precio=12000, dosis=450, tipo_animal="porcino")

    producto_control1 = ControlPlagas(
        registro_ICA="ICA789",
        nombre="InsectiKill",
        frecuencia_aplicacion="Semanal",
        precio=25000,
        periodo_carencia=15
    )

    producto_control2 = Fertilizante(
        registro_ICA="ICA456",
        nombre="SuperGrow",
        frecuencia_aplicacion="Quincenal",
        precio=18000,
        ultima_apliacion="2025-04-15"
    )

    # Crear facturas
    factura1 = Factura(
        cliente=cliente,
        fecha="2025-04-18",
        productos=[antibiotico1, producto_control1]
    )

    factura2 = Factura(
        cliente=cliente,
        fecha="2025-04-19",
        productos=[antibiotico2, producto_control2]
    )

    # Verificar asociación
    print(f"Cliente: {cliente.nombre}")
    print(f"Número de facturas: {len(cliente.facturas)}")

    # Imprimir detalles de las facturas
    for i, factura in enumerate(cliente.facturas, start=1):
        print(f"\nFactura {i}:")
        for producto in factura._Factura__productos:
            print(f"- {producto.nombre}: ${producto.precio}")


    print("\nBreak Point")


if __name__ == "__main__":
    main()
