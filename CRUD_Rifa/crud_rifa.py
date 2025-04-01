import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # o tu usuario
        password="1234",  # o tu contraseña
        database="Poliapuestas"
    )

# CREATEgit
def crear_rifa(data):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
    INSERT INTO Rifa (
        id_boleto, valor_boleto, fecha_ejecucion_sorteo, numero_aleatorio_ganador,
        nombre_rifa, fecha_inicio, fecha_fin_rifa,
        premio_principal, premio_secundario, premio_terciario,
        numero_max_participantes, numero_seleccionado_rifa
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, data)
    conexion.commit()
    print("✅ Rifa creada con éxito.")
    cursor.close()
    conexion.close()

# READ con tabla
def leer_rifas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Rifa")
    resultados = cursor.fetchall()

    if resultados:
        encabezados = [desc[0] for desc in cursor.description]
        print("\n📋 Rifas registradas:")
        print(tabulate(resultados, headers=encabezados, tablefmt="grid"))
    else:
        print("⚠️ No hay rifas registradas.")

    cursor.close()
    conexion.close()

# UPDATE
def actualizar_rifa(id_rifa, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Rifa SET nombre_rifa = %s WHERE id_rifa = %s"
    cursor.execute(sql, (nuevo_nombre, id_rifa))
    conexion.commit()
    print("✏️ Rifa actualizada.")
    cursor.close()
    conexion.close()

# DELETE
def eliminar_rifa(id_rifa):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM Rifa WHERE id_rifa = %s"
    try:
        cursor.execute(sql, (id_rifa,))
        conexion.commit()
        print("🗑️ Rifa eliminada.")
    except mysql.connector.IntegrityError:
        print("❌ No se puede eliminar: la rifa tiene boletos relacionados.")
    cursor.close()
    conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    nueva_rifa = (
        1, 10.0, '2025-04-10 10:00:00', 42, 'Rifa Test',
        '2025-04-01', '2025-04-09', 'TV 50"', 'Celular', 'Audífonos',
        100, 0
    )
    crear_rifa(nueva_rifa)       # INSERTA UNA RIFA
    leer_rifas()                 # MUESTRA TODAS LAS RIFAS
    actualizar_rifa(1, 'Rifa actualizada')  # ACTUALIZA NOMBRE
    leer_rifas()                 # VERIFICAR CAMBIO
    eliminar_rifa(1)             # ELIMINA RIFA
    leer_rifas()                 # DEBERÍA SALIR VACÍA
