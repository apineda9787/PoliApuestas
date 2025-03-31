import database.__init__ as db
import UsuarioDAO as p
import DeporteDAO as d

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Deportes")
        print("3. Salir")
        
        opcion_principal = input("Seleccione una opción: ")
        
        if opcion_principal == "1":
            menu_usuarios()
        elif opcion_principal == "2":
            menu_deportes()
        elif opcion_principal == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def menu_usuarios():
    while True:
        print("\n--- Menú CRUD de Usuarios ---")
        print("1. Mostrar todos los usuarios")
        print("2. Buscar usuario por ID")
        print("3. Buscar usuario por Nombre")
        print("4. Crear un nuevo usuario")
        print("5. Actualizar un usuario")
        print("6. Eliminar un usuario")
        print("7. Volver al menú principal")

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
            break
        else:
            print("Opción no válida, intente de nuevo.")

def menu_deportes():
    while True:
        print("\n--- Menú CRUD de Deportes ---")
        print("1. Mostrar todos los deportes")
        print("2. Buscar deporte por ID")
        print("3. Crear un nuevo deporte")
        print("4. Actualizar un deporte")
        print("5. Eliminar un deporte")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            d.findAll()
        elif opcion == "2":
            id_deporte = input("Digite el ID del deporte a buscar: ")
            d.buscarDeportePorId(id_deporte)
        elif opcion == "3":
            id_deporte = input("Digite el ID del nuevo deporte: ")
            nombre_deporte = input("Digite el nombre del nuevo deporte: ")
            d.crearDeporte(id_deporte, nombre_deporte)
        elif opcion == "4":
            id_deporte = input("Digite el ID del deporte a actualizar: ")
            nombre_deporte = input("Digite el nuevo nombre del deporte: ")
            d.editarDeporte(id_deporte, nombre_deporte)
        elif opcion == "5":
            id_deporte = input("Digite el ID del deporte a eliminar: ")
            d.eliminarDeporte(id_deporte)
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()