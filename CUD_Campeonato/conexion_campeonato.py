import crud_campeonato as c

def main() -> int:
    try:
        print("\n📋 Campeonatos registrados:")
        c.leer_campeonatos()

        print("\n📝 Crear nuevo campeonato")
        id_deporte = int(input("Ingrese el ID del deporte: "))
        id_partido = int(input("Ingrese el ID del partido: "))
        nombre = input("Ingrese el nombre del campeonato: ")
        c.crear_campeonato((id_deporte, id_partido, nombre))

        print("\n📋 Campeonatos después de crear:")
        c.leer_campeonatos()

        print("\n✏️ Actualizar nombre de campeonato")
        idU = int(input("Ingrese el ID del campeonato a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del campeonato: ")
        c.actualizar_nombre_campeonato(idU, nuevo_nombre)

        print("\n📋 Campeonatos después de actualizar:")
        c.leer_campeonatos()

        print("\n🗑️ Eliminar campeonato")
        idE = int(input("Ingrese el ID del campeonato a eliminar: "))
        c.eliminar_campeonato(idE)

        print("\n📋 Campeonatos después de eliminar:")
        c.leer_campeonatos()

    except ValueError:
        print("❌ Entrada no válida. Asegúrate de usar números donde se requiere.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
