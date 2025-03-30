import mysql.connector # pip install mysql-connector-python

# Esta clase se encarga de la conexión a la base de datos y de las operaciones CRUD sobre la tabla persona
# Se utiliza la librería mysql-connector-python para conectarse a la base de datos MySQL

# Esta función se encarga de la conexión a la base de datos y devuelve el objeto de conexión.
def getConnection():
    conn = None
    try:
        conn = mysql.connector.connect(user="root", password="Thommy1945*", host="localhost", database="poli_apuestas", port="3306")
    except:
        print("Error: No se estableción la conexión a la base de datos.")
        return 0
    print("Conectado a la base de datos.")
    return conn

# Esta función se encarga de cerrar la conexión a la base de datos.
def unconnection(conn):
    conn.close()

# This function is used to find all persons in the database and print the result to the console.
def findAll():
    conn = getConnection()
    c = conn.cursor()

    personas = """SELECT * FROM usuario"""

    c.execute(personas)

    personasData = c.fetchall()

    for p in personasData:
        print(p)

    unconnection(conn)

# This function is used to search for a person by their name in the database and print the result to the console.
def buscarPersonaPorNombre(nombre):
    conn = getConnection()
    c = conn.cursor()

    personas = """SELECT * FROM usuario as p WHERE p.nombre LIKE %s"""
    val = ("%{}%".format(nombre),)

    c.execute(personas, val)

    personasData = c.fetchall()

    for p in personasData:
        print(p)

    unconnection(conn)

# This function is used to search for a person by their ID in the database and print the result to the console.
def buscarPersonaPorId(id_usuario):
    conn = getConnection()
    c = conn.cursor()

    id_usuario = int(id_usuario)
    personas = """SELECT * FROM usuario as p WHERE id_usuario = %s"""
    val = (id_usuario,)

    c.execute(personas, val)

    personasData = c.fetchall()

    for p in personasData:
        print(p)

    unconnection(conn)

# This function is used to create a new person in the database.
def crearPersona(id_usuario, nombre, correo, contraseña, saldo_disponible):
    conn = getConnection()
    c = conn.cursor()
    personaInsert = """INSERT into usuario (id_usuario, nombre, correo, contraseña, saldo_disponible) VALUES (%s, %s, 
    %s, %s, %s)"""
    val = (id_usuario, nombre, correo, contraseña, saldo_disponible)
    print(personaInsert)
    c.execute(personaInsert, val)
    conn.commit()
    print(c.rowcount, "record inserted.")
    unconnection(conn)

# This function is used to update a person in the database.
def editarPersona(id_usuario, nombre, correo, contraseña, saldo_disponible):
    conn = getConnection()
    c = conn.cursor()

    try:
        # Convertir id_usuario y saldo_disponible a los tipos adecuados
        id_usuario = int(id_usuario)
        saldo_disponible = float(saldo_disponible)
    except ValueError:
        print("Error: El ID debe ser un número entero y el saldo debe ser un número decimal.")
        return

    try:
        # Verificar si el usuario existe
        c.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
        usuario = c.fetchone()

        if not usuario:
            print(f"Error: El usuario con ID {id_usuario} no existe.")
            return

        print(f"Datos actuales del usuario: {usuario}")

        # Preparar la consulta de actualización
        personaUpdate = """UPDATE usuario 
                           SET nombre = %s, correo = %s, contraseña = %s, saldo_disponible = %s 
                           WHERE id_usuario = %s"""
        val = (nombre, correo, contraseña, saldo_disponible, id_usuario)

        # Ejecutar la actualización
        c.execute(personaUpdate, val)
        conn.commit()

        # Verificar si la actualización afectó filas
        if c.rowcount > 0:
            print(f"{c.rowcount} registro(s) actualizado(s).")
        else:
            print("No se realizaron cambios. ¿Ingresaste los mismos datos?")

    except Exception as e:
        print(f"Error al actualizar usuario: {e}")

    finally:
        unconnection(conn)  # Cerrar conexión al finalizar


# This function is used to delete a person in the database.
def eliminarPersona(id_usuario):
    conn = getConnection()
    c = conn.cursor()
    personaDelete = """DELETE FROM usuario WHERE id_usuario = %s"""
    val = (id_usuario,)
    print(personaDelete)
    c.execute(personaDelete, val)
    conn.commit()
    print(c.rowcount, "record deleted.")
    unconnection(conn)
