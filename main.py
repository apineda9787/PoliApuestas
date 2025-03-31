import database.__init__ as db
import UsuarioDAO as p
import DeporteDAO as d
import RifaDAO as r

# This script is the main entry point for the application, providing a menu-driven interface for user interaction.
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Deportes")
        print("3. Gestión de Rifas")
        print("4. Salir")
        
        opcion_principal = input("Seleccione una opción: ")
        
        if opcion_principal == "1":
            menu_usuarios()
        elif opcion_principal == "2":
            menu_deportes()
        elif opcion_principal == "3":
            menu_rifas()
        elif opcion_principal == "4":
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

# Menú de gestión de rifas
def menu_rifas():
    while True:
        print("\n--- Menú CRUD de Rifas ---")
        print("1. Mostrar todas las rifas")
        print("2. Buscar rifa por ID")
        print("3. Crear una nueva rifa")
        print("4. Actualizar una rifa")
        print("5. Eliminar una rifa")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            r.findAll()
        elif opcion == "2":
            id_rifa = input("Digite el ID de la rifa a buscar: ")
            r.obtener_rifa_por_id(id_rifa)
        elif opcion == "3":
            print("\nIngrese los datos de la nueva rifa:")
            id_boleto = input("ID del boleto: ")
            valor_boleto = input("Valor del boleto: ")
            fecha_ejecucion_sorteo = input("Fecha de ejecución del sorteo (YYYY-MM-DD HH:MM:SS): ")
            numero_aleatorio_ganador = input("Número aleatorio ganador: ")
            nombre_rifa = input("Nombre de la rifa: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin_rifa = input("Fecha de fin de la rifa (YYYY-MM-DD): ")
            premio_principal = input("Premio principal: ")
            premio_secundario = input("Premio secundario (opcional): ")
            premio_terciario = input("Premio terciario (opcional): ")
            numero_max_participantes = input("Número máximo de participantes: ")
            numero_seleccionado_rifa = input("Número seleccionado para la rifa: ")

            r.crear_rifa(id_boleto, valor_boleto, fecha_ejecucion_sorteo, numero_aleatorio_ganador, 
                         nombre_rifa, fecha_inicio, fecha_fin_rifa, premio_principal, 
                         premio_secundario, premio_terciario, numero_max_participantes, 
                         numero_seleccionado_rifa)
        elif opcion == "4":
            id_rifa = input("Digite el ID de la rifa a actualizar: ")
            print("Ingrese los nuevos datos (deje vacío para no modificar):")
            nuevo_nombre = input("Nuevo nombre de la rifa: ")
            nuevo_premio_principal = input("Nuevo premio principal: ")
            r.actualizar_rifa(id_rifa, nuevo_nombre, nuevo_premio_principal)  # Adaptar a los campos editables
        elif opcion == "5":
            id_rifa = input("Digite el ID de la rifa a eliminar: ")
            r.eliminar_rifa(id_rifa)
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente de nuevo.")            

if __name__ == "__main__":
    main()