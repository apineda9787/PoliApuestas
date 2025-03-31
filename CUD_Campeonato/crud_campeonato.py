import mysql.connector
from mysql.connector import Error, IntegrityError
from tabulate import tabulate

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Poliapuestas"
    )

# CREATE
def crear_campeonato(data):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
    INSERT INTO Campeonato (
        id_deporte, id_partido, nombre_campeonato
    ) VALUES (%s, %s, %s)
    """
    cursor.execute(sql, data)
    conexion.commit()
    print("✅ Campeonato creado con éxito.")
    cursor.close()
    conexion.close()

# READ
def leer_campeonatos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Campeonato")
    resultados = cursor.fetchall()
    if resultados:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    else:
        print("⚠️ No hay campeonatos registrados.")
    cursor.close()
    conexion.close()

# UPDATE
def actualizar_nombre_campeonato(id_campeonato, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Campeonato SET nombre_campeonato = %s WHERE id_campeonato = %s"
    cursor.execute(sql, (nuevo_nombre, id_campeonato))
    conexion.commit()
    print("✏️ Campeonato actualizado.")
    cursor.close()
    conexion.close()

# DELETE con manejo de integridad referencial
def eliminar_campeonato(id_campeonato):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        sql = "DELETE FROM Campeonato WHERE id_campeonato = %s"
        cursor.execute(sql, (id_campeonato,))
        conexion.commit()
        if cursor.rowcount > 0:
            print("🗑️ Campeonato eliminado.")
        else:
            print("⚠️ No se encontró el campeonato con ese ID.")
    except IntegrityError:
        print("❌ No se puede eliminar: existen apuestas relacionadas con este campeonato.")
    finally:
        cursor.close()
        conexion.close()

# PRUEBA DIRECTA
if __name__ == "__main__":
    print("📋 Campeonatos actuales:")
    leer_campeonatos()

    # Descomenta según la prueba que quieras hacer:

    # crear_campeonato((1, 1, 'Copa América Universitaria'))
    # actualizar_nombre_campeonato(1, 'Copa Nacional Universitaria')
    eliminar_campeonato(1)

    print("📋 Campeonatos después de la acción:")
    leer_campeonatos()
