import crud_rifa as r
from tabulate import tabulate

def main() -> int:
    try:
        print("\n📋 Rifas actuales:")
        r.leer_rifas()

        print("\n📝 Crear nueva rifa")
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

        r.crear_rifa(nueva_rifa)

        print("\n📋 Rifas después de crear:")
        r.leer_rifas()

        print("\n✏️ Actualizar rifa")
        idU = int(input("ID de la rifa a actualizar: "))
        nuevo_nombre = input("Nuevo nombre de la rifa: ")
        r.actualizar_rifa(idU, nuevo_nombre)

        print("\n📋 Rifas después de actualizar:")
        r.leer_rifas()

        print("\n🗑️ Eliminar rifa")
        idE = int(input("ID de la rifa a eliminar: "))
        r.eliminar_rifa(idE)

        print("\n📋 Rifas después de eliminar:")
        r.leer_rifas()

    except ValueError:
        print("❌ Error: Entrada inválida.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
