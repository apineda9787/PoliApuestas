import crud_boleto as b
from tabulate import tabulate

def main() -> int:
    try:
        print("\n📋 Boletos actuales:")
        b.leer_boletos()

        print("\n📝 Crear nuevo boleto")
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

        b.crear_boleto(nuevo_boleto)
        print("\n📋 Boletos después de crear:")
        b.leer_boletos()

        print("\n✏️ Editar boleto")
        idU = int(input("ID del boleto a actualizar: "))
        nuevo_nombre_rifa = input("Nuevo nombre para la rifa en el boleto: ")
        b.actualizar_nombre_rifa(idU, nuevo_nombre_rifa)

        print("\n📋 Boletos después de actualizar:")
        b.leer_boletos()

        print("\n🗑️ Borrar boleto")
        idE = int(input("ID del boleto a eliminar: "))
        b.eliminar_boleto(idE)

        print("\n📋 Boletos después de eliminar:")
        b.leer_boletos()

    except ValueError:
        print("❌ Error: Entrada no válida.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
