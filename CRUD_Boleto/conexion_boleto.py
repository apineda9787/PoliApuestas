import crud_boleto as b

def main() -> int:
    try:
        # Mostrar todos los boletos
        b.leer_boletos()

        # Crear nuevo boleto
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

        # Mostrar boletos después de crear
        b.leer_boletos()

        # Buscar boletos por nombre de rifa
        print("\n🔎 Buscar boleto por nombre de rifa")
        nombre_busqueda = input("Digite el nombre de la rifa a buscar: ")
        b.buscar_boleto_por_nombre_rifa(nombre_busqueda)

        # Editar nombre de la rifa
        print("\n✏️ Editar nombre de la rifa")
        idU = int(input("Digite el ID del boleto a actualizar: "))
        nuevo_nombre_rifa = input("Digite el nuevo nombre de la rifa: ")
        b.actualizar_nombre_rifa(idU, nuevo_nombre_rifa)

        # Mostrar boletos después de actualizar
        b.leer_boletos()

        # Eliminar boleto
        print("\n🗑️ Borrar boleto")
        idE = int(input("Digite el ID del boleto a eliminar: "))
        b.eliminar_boleto(idE)

        # Mostrar boletos después de eliminar
        b.leer_boletos()

    except ValueError:
        print("❌ Error: Valores no válidos.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
