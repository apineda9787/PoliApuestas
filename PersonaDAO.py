import mysql.connector
#se instala con pip install mysql-connector-python
def getConnection():
    conn = None
    try:
        conn = mysql.connector.connect(user="root", password="psswrd", host="localhost", database="agenda", port="3306")
    except:
        print("no se puede conectar a la base de datos")
        return 0
    print("conectado")
    return conn


def unconnection(conn):
    conn.close()

def findAll():
    conn = getConnection()
    c = conn.cursor()

    personas = """SELECT * FROM agenda.persona"""

    c.execute(personas)

    personasData = c.fetchall()

    for p in personasData:
        print(p)

    unconnection(conn)

def buscarPersonaPorNombre(nombre):
    conn = getConnection()
    c = conn.cursor()

    personas = """SELECT * FROM agenda.persona as p WHERE p.nombre LIKE %s"""
    val = ("%{}%".format(nombre),)

    c.execute(personas, val)

    personasData = c.fetchall()

    for p in personasData:
        print(p)

    unconnection(conn)

def buscarPersonaPorId(id):
    conn = getConnection()
    c = conn.cursor()

    personas = """SELECT * FROM agenda.persona as p WHERE p.idpersona = %s"""
    val = (id)

    c.execute(personas, val)

    personasData = c.fetchall()

    for p in personasData:
        print(p)

    unconnection(conn)


def crearPersona(id, nombre, apellido, email, numDocumento):
    conn = getConnection()
    c = conn.cursor()
    personaInsert = """INSERT into persona (idpersona, nombre, apellido, email, num_documento) VALUES (%s, %s, 
    %s, %s, %s)"""
    val = (id, nombre, apellido, email, numDocumento)
    print(personaInsert)
    c.execute(personaInsert, val)
    conn.commit()
    print(c.rowcount, "record inserted.")
    unconnection(conn)

def editarPersona(nombre, apellido, email, numDocumento, id):
    conn = getConnection()
    c = conn.cursor()
    personaUpdate = """UPDATE persona SET nombre = %s, 
    apellido = %s, 
    email = %s, 
    num_documento = %s 
    WHERE idpersona = %s"""
    val = (nombre, apellido, email, numDocumento, id)
    print(personaUpdate)
    c.execute(personaUpdate, val)
    conn.commit()
    print(c.rowcount, "record updated.")
    unconnection(conn)

def eliminarPersona(id):
    conn = getConnection()
    c = conn.cursor()
    personaDelete = """DELETE FROM persona WHERE idpersona = %s"""
    val = (id,)
    print(personaDelete)
    c.execute(personaDelete, val)
    conn.commit()
    print(c.rowcount, "record deleted.")
    unconnection(conn)
