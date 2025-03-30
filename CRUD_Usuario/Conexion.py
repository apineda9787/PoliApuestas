import PersonaDAO as p
def main()->int:
    try:
        p.findAll()
        id = input("digite el id ")
        nombre = input("digite el nombre ")
        apellido = input("digite el apellido ")
        email = input("digite el email ")
        numDocumento = input("digite el número de documento ")
        p.crearPersona(id, nombre, apellido, email, numDocumento)
        p.findAll()
        print("búsqueda!")
        nombreB = input("digite el nombre a buscar ")
        p.buscarPersonaPorNombre(nombreB)
        print("editar")
        idU = input("digite el id a actualizar ")
        nombreU = input("digite el nombre actualizado ")
        apellidoU = input("digite el apellido ")
        emailU = input("digite el email ")
        numDocumentoU = input("digite el número de documento ")
        p.editarPersona(nombreU, apellidoU, emailU, numDocumentoU, idU)
        p.findAll()
        print("Borrar!")
        idE = input("digite el id a eliminar ")
        p.eliminarPersona(idE)
        p.findAll()
    except ValueError:
        print("Valores no validos")

if __name__ == "__main__":
    main()