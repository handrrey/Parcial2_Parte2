from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico
from crud.cliente_crud import clientes_registrados

# Listas de productos disponibles
antibioticos_disponibles = [
    Antibiotico("AmoxiVet", 15000, 500, "bovino"),
    Antibiotico("PorciPen", 12000, 450, "porcino"),
    Antibiotico("CapriCure", 14000, 470, "caprino"),
    Antibiotico("Bovimix", 16000, 510, "bovino"),
    Antibiotico("PorciMix", 13000, 480, "porcino")
]

fertilizantes_disponibles = [
    Fertilizante("ICA001", "FertiMax", "Mensual", 18000, "2025-04-01"),
    Fertilizante("ICA002", "SuperGrow", "Quincenal", 22000, "2025-04-10"),
    Fertilizante("ICA003", "MegaGreen", "Semestral", 25000, "2025-03-20"),
    Fertilizante("ICA004", "EcoFert", "Mensual", 17000, "2025-04-05"),
    Fertilizante("ICA005", "UltraFert", "Trimestral", 19000, "2025-04-15")
]

productos_control_plagas_disponibles = [
    ControlPlagas("ICA101", "InsectAway", "Semanal", 20000, 10),
    ControlPlagas("ICA102", "BugKill", "Mensual", 22000, 12),
    ControlPlagas("ICA103", "PlagaStop", "Quincenal", 25000, 8),
    ControlPlagas("ICA104", "TermiGone", "Trimestral", 27000, 15),
    ControlPlagas("ICA105", "PestOut", "Semestral", 23000, 20)
]

facturas_registradas = []

def vender_productos(cedula_cliente: str, productos_seleccionados: list, fecha: str):
    cliente = clientes_registrados.get(cedula_cliente)
    if not cliente:
        print("Cliente no encontrado.")
        return

    if not productos_seleccionados:
        print("No se seleccionaron productos.")
        return

    factura = Factura(
        cliente=cliente,
        fecha=fecha,
        productos=productos_seleccionados
    )

    facturas_registradas.append(factura)
    total = sum(producto.precio for producto in productos_seleccionados)

    print("\n----- RESUMEN DE FACTURA -----")
    print(f"Cliente: {cliente.nombre} (Cédula: {cliente.cedula})")
    print(f"Fecha: {fecha}")
    print("\nProductos:")
    for i, producto in enumerate(productos_seleccionados, 1):
        print(f"{i}. {producto.nombre} - Precio: ${producto.precio}")
    print(f"\nTotal a pagar: ${total}")
    print("-----------------------------")


def obtener_producto(tipo_producto: str, seleccion: int):
    if tipo_producto == "antibiotico":
        if 1 <= seleccion <= len(antibioticos_disponibles):
            return antibioticos_disponibles[seleccion - 1]
    elif tipo_producto == "fertilizante":
        if 1 <= seleccion <= len(fertilizantes_disponibles):
            return fertilizantes_disponibles[seleccion - 1]
    elif tipo_producto == "control plagas":
        if 1 <= seleccion <= len(productos_control_plagas_disponibles):
            return productos_control_plagas_disponibles[seleccion - 1]
    return None

def mostrar_productos(tipo_producto):
    if tipo_producto == "antibiotico":
        print("\nAntibióticos disponibles:")
        for idx, producto in enumerate(antibioticos_disponibles, start=1):
            print(
                f"{idx}. {producto.nombre} - Dosis: {producto.dosis}mg - Tipo Animal: {producto.tipo_animal} - Precio: ${producto.precio}")
        return len(antibioticos_disponibles)

    elif tipo_producto == "fertilizante":
        print("\nFertilizantes disponibles:")
        for idx, producto in enumerate(fertilizantes_disponibles, start=1):
            print(
                f"{idx}. {producto.nombre} - Registro ICA: {producto.registro_ICA} - Frecuencia: {producto.frecuencia_aplicacion} - Precio: ${producto.precio}")
        return len(fertilizantes_disponibles)

    elif tipo_producto == "control plagas":
        print("\nProductos de Control de Plagas disponibles:")
        for idx, producto in enumerate(productos_control_plagas_disponibles, start=1):
            print(
                f"{idx}. {producto.nombre} - Registro ICA: {producto.registro_ICA} - Frecuencia: {producto.frecuencia_aplicacion} - Carencia: {producto.periodo_carencia} días - Precio: ${producto.precio}")
        return len(productos_control_plagas_disponibles)
    return 0