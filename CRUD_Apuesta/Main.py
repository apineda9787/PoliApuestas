import ApuestaDAO as dao
from tabulate import tabulate 

def Main():
    while True:
        print("\n>>MENÚ CRUD - Tabla Apuesta<<")
        print("1. Ver todas las apuestas")
        print("2. Crear una nueva apuesta")
        print("3. Actualizar una apuesta")
        print("4. Eliminar una apuesta")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\nListado de Apuestas:")
            apuestas = dao.obtener_apuestas()
            print(tabulate(apuestas, headers="keys", tablefmt="fancy_grid"))

        
        elif opcion == "2":
            id_usuario = int(input("ID Usuario: "))
            id_deporte = int(input("ID Deporte: "))
            id_campeonato = int(input("ID Campeonato: "))
            id_partido = int(input("ID Partido: "))
            valor_boleto = float(input("Valor Boleto: "))
            marcador1 = int(input("Marcador Equipo 1: "))
            marcador2 = int(input("Marcador Equipo 2: "))
            dao.crear_apuesta(id_usuario, id_deporte, id_campeonato, id_partido, valor_boleto, marcador1, marcador2)
        
        elif opcion == "3":
            id_apuesta = int(input("ID de la Apuesta a actualizar: "))
            valor_boleto = float(input("Nuevo Valor Boleto: "))
            marcador1 = int(input("Nuevo Marcador Equipo 1: "))
            marcador2 = int(input("Nuevo Marcador Equipo 2: "))
            dao.actualizar_apuesta(id_apuesta, valor_boleto, marcador1, marcador2)
        
        elif opcion == "4":
            id_apuesta = int(input("ID de la Apuesta a eliminar: "))
            dao.eliminar_apuesta(id_apuesta)
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    Main()
