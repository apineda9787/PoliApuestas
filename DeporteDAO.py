import mysql.connector  # pip install mysql-connector-python

# Clase DeporteDAO para la gestión de la tabla Deporte
def getConnection():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="Thommy1945*",
            host="localhost",
            database="poli_apuestas",
            port="3306"
        )
        print("Conectado a la base de datos.")
        return conn
    except Exception as e:
        print("Error: No se estableció la conexión a la base de datos.", e)
        return None

# This function is used to close the database connection.
def unconnection(conn):
    if conn:
        conn.close()

# Método para obtener todos los deportes
def findAll():
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM deporte")
    deportes = cursor.fetchall()
    
    for deporte in deportes:
        print(deporte)
    
    unconnection(conn)

# Método para buscar un deporte por nombre
def buscarDeportePorNombre(nombre):
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    query = "SELECT * FROM Deporte WHERE nombre_deporte LIKE %s"
    val = (f"%{nombre}%",)
    
    cursor.execute(query, val)
    deportes = cursor.fetchall()
    
    for deporte in deportes:
        print(deporte)
    
    unconnection(conn)

# Método para buscar un deporte por ID
def buscarDeportePorId(id_deporte):
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    query = "SELECT * FROM Deporte WHERE id_deporte = %s"
    val = (id_deporte,)
    
    cursor.execute(query, val)
    deporte = cursor.fetchone()
    
    if deporte:
        print(deporte)
    else:
        print("No se encontró el deporte con ID:", id_deporte)
    
    unconnection(conn)

# Método para crear un nuevo deporte
def crearDeporte(id_deporte, nombre_deporte):
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    deporteInsert = "INSERT INTO Deporte (id_deporte, nombre_deporte) VALUES (%s, %s)"
    val = (id_deporte, nombre_deporte)
    print
    cursor.execute(deporteInsert, val)
    conn.commit()
    print(cursor.rowcount, "Deporte creado en la Base de Datos.")
    unconnection(conn)

# Método para actualizar un deporte
def editarDeporte(id_deporte, nombre_deporte):
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    query = "UPDATE Deporte SET nombre_deporte = %s WHERE id_deporte = %s"
    val = (nombre_deporte, id_deporte)
    
    cursor.execute(query, val)
    conn.commit()
    
    if cursor.rowcount > 0:
        print(cursor.rowcount, "registro actualizado.")
    else:
        print("No se realizaron cambios. ¿Ingresaste los mismos datos?")
    
    unconnection(conn)

# Método para eliminar un deporte
def eliminarDeporte(id_deporte):
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    query = "DELETE FROM Deporte WHERE id_deporte = %s"
    val = (id_deporte,)
    
    cursor.execute(query, val)
    conn.commit()
    print(cursor.rowcount, "registro eliminado.")
    
    unconnection(conn)