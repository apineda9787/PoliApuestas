import crud_boleto as dao
from tabulate import tabulate

def main():
    while True:
        print("\n>> MENÚ CRUD - Tabla Boleto <<")
        print("1. Ver todos los boletos")
        print("2. Crear un nuevo boleto")
        print("3. Actualizar nombre de rifa de un boleto")
        print("4. Eliminar un boleto")
        print("5. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            print("\n📋 Listado de Boletos:")
            dao.leer_boletos()

        elif opcion == "2":
            try:
                print("\n📝 Crear Nuevo Boleto")
                valor_boleto = float(input("Valor del boleto: "))
                fecha_apertura = input("Fecha apertura boleto (YYYY-MM-DD HH:MM:SS): ")
                fecha_cierre = input("Fecha cierre boleto (YYYY-MM-DD HH:MM:SS): ")
                id_venta = int(input("ID de la venta: "))
                fecha_venta = input("Fecha de venta (YYYY-MM-DD HH:MM:SS): ")
                monto_venta = float(input("Monto de la venta: "))
                id_apuesta = int(input("ID de la apuesta: "))
                fecha_inicio_apuesta = input("Fecha inicio apuesta (YYYY-MM-DD HH:MM:SS): ")
                marcador1 = int(input("Marcador primer equipo: "))
                marcador2 = int(input("Marcador segundo equipo: "))
                id_rifa = int(input("ID de la rifa: "))
                fecha_ejecucion = input("Fecha ejecución sorteo (YYYY-MM-DD HH:MM:SS): ")
                nombre_rifa = input("Nombre de la rifa: ")
                numero_seleccionado = int(input("Número seleccionado en la rifa: "))

                nuevo_boleto = (
                    valor_boleto, fecha_apertura, fecha_cierre,
                    id_venta, fecha_venta, monto_venta, id_apuesta, fecha_inicio_apuesta,
                    marcador1, marcador2, id_rifa,
                    fecha_ejecucion, nombre_rifa, numero_seleccionado
                )

                dao.crear_boleto(nuevo_boleto)
            except ValueError:
                print("❌ Error: Entrada inválida. Intenta de nuevo.")

        elif opcion == "3":
            try:
                print("\n✏️ Actualizar nombre de rifa")
                id_boleto = int(input("ID del boleto a actualizar: "))
                nuevo_nombre = input("Nuevo nombre de la rifa: ")
                dao.actualizar_nombre_rifa(id_boleto, nuevo_nombre)
            except ValueError:
                print("❌ Error: ID inválido.")

        elif opcion == "4":
            try:
                print("\n🗑️ Eliminar boleto")
                id_boleto = int(input("ID del boleto a eliminar: "))
                dao.eliminar_boleto(id_boleto)
            except ValueError:
                print("❌ Error: ID inválido.")

        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
