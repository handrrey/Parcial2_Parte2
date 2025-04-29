from crud.cliente_crud import registrar_cliente, buscar_por_cedula, clientes_registrados
from crud.producto_crud import vender_producto, antibioticos_disponibles, fertilizantes_disponibles, productos_control_plagas_disponibles


def menu():
    while True:

        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Cliente")
        print("2. Vender Producto")
        print("3. Buscar Facturas por Cédula")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            while True:
                cedula = input("Cédula del cliente: ")
                if cedula.isdigit() and int(cedula) > 0:
                    break
                else:
                    print("La cédula debe ser un número entero positivo.")
            registrar_cliente(nombre, cedula)

        elif opcion == "2":
            cedula = input("Cédula del cliente: ")
            if not (cedula.isdigit() and int(cedula) > 0):
                print("La cédula debe ser un número entero positivo.")
                input("Presione Enter para continuar...")
                continue
            if cedula not in clientes_registrados:
                print("La cédula ingresada no corresponde a ningún cliente registrado. Regístrelo primero.")
                input("Presione Enter para continuar...")
                continue

            tipo_producto = input("Tipo de producto (antibiotico, fertilizante, control_plagas): ").lower()

            if tipo_producto == "antibiotico":
                print("\nAntibióticos disponibles:")
                for idx, producto in enumerate(antibioticos_disponibles, start=1):
                    print(f"{idx}. {producto.nombre} - Dosis: {producto.dosis}mg - Tipo Animal: {producto.tipo_animal}")

            elif tipo_producto == "fertilizante":
                print("\nFertilizantes disponibles:")
                for idx, producto in enumerate(fertilizantes_disponibles, start=1):
                    print(f"{idx}. {producto.nombre} - Registro ICA: {producto.registro_ICA} - Frecuencia: {producto.frecuencia_aplicacion}")

            elif tipo_producto == "control_plagas":
                print("\nProductos de Control de Plagas disponibles:")
                for idx, producto in enumerate(productos_control_plagas_disponibles, start=1):
                    print(f"{idx}. {producto.nombre} - Registro ICA: {producto.registro_ICA} - Frecuencia: {producto.frecuencia_aplicacion} - Carencia: {producto.periodo_carencia} días")
            else:
                print("Tipo de producto no válido.")
                input("Presione Enter para continuar...")
                continue

            try:
                seleccion = int(input("Seleccione el número del producto: "))
                nombre_producto = input("Nombre del producto (confirme el nombre): ")
                while True:
                    try:
                        precio = float(input("Precio del producto: "))
                        if precio <= 0:
                            print("El precio debe ser positivo.")
                            continue
                        break
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                fecha = input("Fecha de la compra (YYYY-MM-DD): ")
                vender_producto(cedula, tipo_producto, seleccion, fecha, precio)
            except ValueError:
                print("Selección inválida.")
                input("Presione Enter para continuar...")

        elif opcion == "3":
            while True:
                cedula = input("Ingrese la cédula: ")
                if cedula.isdigit() and int(cedula) > 0:
                    break
                else:
                    print("La cédula debe ser un número entero positivo.")
            buscar_por_cedula(cedula)
            input("Presione Enter para continuar...")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()
