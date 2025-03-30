import PersonaDAO as p

def main()->int:
    try:
        p.findAll()
        id_usuario = input("Digite el id: ")
        nombre = input("Digite el nombre: ")
        correo = input("Digite el correo:")
        contraseña = input("Digite la contraseña: ")
        saldo_disponible = input("Digite el saldo disponible: ")
        p.crearPersona(id_usuario, nombre, correo, contraseña, saldo_disponible)

        p.findAll()
        print("búsqueda!")
        nombreB = input("digite el nombre a buscar ")
        p.buscarPersonaPorNombre(nombreB)
        print("editar")
        idU = input("Digite el ID a actualizar:")
        nombreU = input("Digite el nombre actualizado: ")
        correoU = input("Digite el correo: ")
        contraseñaU = input("Digite la contraseña: ")
        saldo_disponibleU = input("Digite el saldo disponible: ")
        p.editarPersona(idU, nombreU, correoU, contraseñaU, saldo_disponibleU)
        p.findAll()
        print("Borrar!")
        idE = input("digite el id a eliminar ")
        p.eliminarPersona(idE)
        p.findAll()
    except ValueError:
        print("Valores no validos")

if __name__ == "__main__":
    main()