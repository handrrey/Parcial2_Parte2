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


def vender_producto(cedula_cliente: str, tipo_producto: str, seleccion: int, fecha: str, precio: float):
    cliente = clientes_registrados.get(cedula_cliente)
    if not cliente:
        print("Cliente no encontrado.")
        return

    producto = None

    if tipo_producto == "antibiotico":
        if 1 <= seleccion <= len(antibioticos_disponibles):
            producto = antibioticos_disponibles[seleccion - 1]
    elif tipo_producto == "fertilizante":
        if 1 <= seleccion <= len(fertilizantes_disponibles):
            producto = fertilizantes_disponibles[seleccion - 1]
    elif tipo_producto == "control_plagas":
        if 1 <= seleccion <= len(productos_control_plagas_disponibles):
            producto = productos_control_plagas_disponibles[seleccion - 1]

    if not producto:
        print("Selección inválida.")
        return

    producto.precio = precio

    factura = Factura(
        cliente=cliente,
        fecha=fecha,
        productos=[producto]
    )

    print(f"Producto '{producto.nombre}' ({tipo_producto}) vendido al cliente {cliente.nombre} el {fecha}.")

