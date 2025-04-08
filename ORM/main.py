# main.py
import db
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ORM.Usuario import Usuario

# Este método crea un nuevo usuario en la base de datos.
# Se le pide al usuario que ingrese su nombre, correo, contraseña y saldo disponible.
def crear_usuario():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")
    saldo = float(input("Saldo disponible: "))
    nuevo_usuario = Usuario(nombre, correo, contraseña, saldo) # Crear una instancia de Usuario con los datos ingresados
    db.session.add(nuevo_usuario) # Agregar el nuevo usuario a la sesión
    db.session.commit() # Confirmar los cambios en la base de datos
    print(" Usuario creado con ID:", nuevo_usuario.id_usuario) # Mostrar el ID del nuevo usuario creado

# Este método lista todos los usuarios en la base de datos.
def listar_usuarios():
    usuarios = db.session.query(Usuario).all() # Obtener todos los usuarios de la base de datos
    print("\n Lista de usuarios:") # Mostrar encabezado de la lista
    for u in usuarios:
        print(u.to_dict())

# Este método actualiza la información de un usuario existente en la base de datos.
def actualizar_usuario():
    id_u = input(" ID del usuario a actualizar: ") # Solicitar ID del usuario a actualizar
    usuario = db.session.query(Usuario).get(id_u) # Buscar el usuario por ID
    if usuario:
        print("Usuario encontrado:", usuario.to_dict()) # Mostrar información del usuario encontrado
        usuario.nombre = input("Nuevo nombre: ") or usuario.nombre # Actualizar nombre si se proporciona uno nuevo
        usuario.correo = input("Nuevo correo: ") or usuario.correo # Actualizar correo si se proporciona uno nuevo
        usuario.contraseña = input("Nueva contraseña: ") or usuario.contraseña
        nuevo_saldo = input("Nuevo saldo disponible: ")
        if nuevo_saldo:
            usuario.saldo_disponible = float(nuevo_saldo) # Actualizar saldo si se proporciona uno nuevo
        db.session.commit() # Confirmar los cambios en la base de datos
        print(" Usuario actualizado.")
    else:
        print(" Usuario no encontrado.")

# Este método elimina un usuario de la base de datos.
def eliminar_usuario():
    id_u = input("ID del usuario a eliminar: ") # Solicitar ID del usuario a eliminar
    usuario = db.session.query(Usuario).get(id_u) # Buscar el usuario por ID
    if usuario: # Si el usuario existe
        db.session.delete(usuario) # Eliminar el usuario de la sesión
        db.session.commit()# Confirmar los cambios en la base de datos
        print(" Usuario eliminado.")
    else:
        print(" Usuario no encontrado.")

def menu():
    while True:
        print("\n MENÚ CRUD DE USUARIOS")
        print("1. Crear Usuario")
        print("2. Listar Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            listar_usuarios()
        elif opcion == '3':
            actualizar_usuario()
        elif opcion == '4':
            eliminar_usuario()
        elif opcion == '5':
            print(" Saliendo del programa.")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")

# Este bloque se ejecuta si el script se ejecuta directamente.
if __name__ == '__main__':
    # Opcional si deseas crear tablas si no existen
    # db.Base.metadata.create_all(db.engine)
    menu()