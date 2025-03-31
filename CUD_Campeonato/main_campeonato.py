import crud_campeonato as dao
from tabulate import tabulate

def Main():
    while True:
        print("\n>>MENÚ CRUD - Tabla Campeonato<<")
        print("1. Ver todos los campeonatos")
        print("2. Crear un nuevo campeonato")
        print("3. Actualizar nombre de campeonato")
        print("4. Eliminar un campeonato")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\nListado de Campeonatos:")
            dao.leer_campeonatos()

        elif opcion == "2":
            try:
                id_deporte = int(input("ID del deporte: "))
                id_partido = int(input("ID del partido: "))
                nombre = input("Nombre del campeonato: ")
                dao.crear_campeonato((id_deporte, id_partido, nombre))
            except ValueError:
                print("❌ Error: Entrada inválida. Intenta de nuevo.")

        elif opcion == "3":
            try:
                id_campeonato = int(input("ID del campeonato a actualizar: "))
                nuevo_nombre = input("Nuevo nombre del campeonato: ")
                dao.actualizar_nombre_campeonato(id_campeonato, nuevo_nombre)
            except ValueError:
                print("❌ Error: Entrada inválida. Intenta de nuevo.")

        elif opcion == "4":
            try:
                id_campeonato = int(input("ID del campeonato a eliminar: "))
                dao.eliminar_campeonato(id_campeonato)
            except ValueError:
                print("❌ Error: Entrada inválida. Intenta de nuevo.")

        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    Main()
