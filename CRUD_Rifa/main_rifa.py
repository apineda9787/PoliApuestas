import crud_rifa as dao
from tabulate import tabulate

def Main():
    while True:
        print("\n>>MENÚ CRUD - Tabla Rifa<<")
        print("1. Ver todas las rifas")
        print("2. Crear una nueva rifa")
        print("3. Actualizar nombre de rifa")
        print("4. Eliminar una rifa")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\nListado de Rifas:")
            dao.leer_rifas()

        elif opcion == "2":
            try:
                id_boleto = int(input("ID del boleto: "))
                valor_boleto = float(input("Valor del boleto: "))
                fecha_ejecucion = input("Fecha y hora del sorteo (YYYY-MM-DD HH:MM:SS): ")
                numero_ganador = int(input("Número aleatorio ganador: "))
                nombre_rifa = input("Nombre de la rifa: ")
                fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha de finalización (YYYY-MM-DD): ")
                premio1 = input("Premio principal: ")
                premio2 = input("Premio secundario: ")
                premio3 = input("Premio terciario: ")
                max_participantes = int(input("Número máximo de participantes: "))
                numero_seleccionado = int(input("Número seleccionado en la rifa: "))

                nueva_rifa = (
                    id_boleto, valor_boleto, fecha_ejecucion, numero_ganador,
                    nombre_rifa, fecha_inicio, fecha_fin,
                    premio1, premio2, premio3,
                    max_participantes, numero_seleccionado
                )

                dao.crear_rifa(nueva_rifa)
            except ValueError:
                print("❌ Error: Entrada inválida.")

        elif opcion == "3":
            try:
                id_rifa = int(input("ID de la rifa a actualizar: "))
                nuevo_nombre = input("Nuevo nombre de la rifa: ")
                dao.actualizar_rifa(id_rifa, nuevo_nombre)
            except ValueError:
                print("❌ Error: Entrada inválida.")

        elif opcion == "4":
            try:
                id_rifa = int(input("ID de la rifa a eliminar: "))
                dao.eliminar_rifa(id_rifa)
            except ValueError:
                print("❌ Error: Entrada inválida.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    Main()
