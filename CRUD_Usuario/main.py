import PersonaDAO as p

def main():
    while True:
        print("\n--- Menú CRUD de Usuarios ---")
        print("1. Mostrar todos los usuarios")
        print("2. Buscar usuario por ID")
        print("3. Buscar usuario por Nombre")
        print("4. Crear un nuevo usuario")
        print("5. Editar un usuario")
        print("6. Eliminar un usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            p.findAll()

        elif opcion == "2":
            id_usuario = input("Digite el ID del usuario a buscar: ")
            p.buscarPersonaPorId(id_usuario)

        elif opcion == "3":
            nombre = input("Digite el nombre del usuario a buscar: ")
            p.buscarPersonaPorNombre(nombre)

        elif opcion == "4":
            id_usuario = input("Digite el ID del nuevo usuario: ")
            nombre = input("Digite el nombre: ")
            correo = input("Digite el correo: ")
            contraseña = input("Digite la contraseña: ")
            saldo_disponible = input("Digite el saldo disponible: ")
            p.crearPersona(id_usuario, nombre, correo, contraseña, saldo_disponible)

        elif opcion == "5":
            id_usuario = input("Digite el ID del usuario a actualizar: ")
            nombre = input("Digite el nuevo nombre: ")
            correo = input("Digite el nuevo correo: ")
            contraseña = input("Digite la nueva contraseña: ")
            saldo_disponible = input("Digite el nuevo saldo disponible: ")
            p.editarPersona(id_usuario, nombre, correo, contraseña, saldo_disponible)


        elif opcion == "6":
            id_usuario = input("Digite el ID del usuario a eliminar: ")
            p.eliminarPersona(id_usuario)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()