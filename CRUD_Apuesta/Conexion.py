import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin123*",
            database="PoliApuestas"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")
        return None
