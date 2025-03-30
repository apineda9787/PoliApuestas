import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Cambia según tu configuración
        password="1234",        # Si tienes contraseña, ponla aquí
        database="Poliapuestas"
    )

# CREATE
def crear_boleto(data):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
    INSERT INTO Boleto (
        valor_boleto, fecha_apertura_boleto, fecha_cierre_boleto,
        id_venta, fecha_venta, monto_venta, id_apuesta, fecha_inicio_apuesta,
        marcador_primer_equipo, marcador_segundo_equipo, id_rifa,
        fecha_ejecucion_sorteo, nombre_rifa, numero_seleccionado_rifa
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, data)
    conexion.commit()
    print("✅ Boleto creado con éxito.")
    cursor.close()
    conexion.close()

# READ
def leer_boletos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Boleto")
    resultados = cursor.fetchall()
    if resultados:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(resultados, headers=headers, tablefmt="grid"))
    else:
        print("⚠️ No hay boletos registrados.")
    cursor.close()
    conexion.close()

# UPDATE
def actualizar_nombre_rifa(id_boleto, nuevo_nombre_rifa):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Boleto SET nombre_rifa = %s WHERE id_boleto = %s"
    cursor.execute(sql, (nuevo_nombre_rifa, id_boleto))
    conexion.commit()
    print("✏️ Nombre de la rifa actualizado en el boleto.")
    cursor.close()
    conexion.close()

# DELETE
def eliminar_boleto(id_boleto):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM Boleto WHERE id_boleto = %s"
    cursor.execute(sql, (id_boleto,))
    conexion.commit()
    print("🗑️ Boleto eliminado.")
    cursor.close()
    conexion.close()

# Prueba de ejemplo
if __name__ == "__main__":
    nuevo_boleto = (
        5000.0, '2025-04-01 10:00:00', '2025-04-10 18:00:00',
        101, '2025-04-05 12:00:00', 5000.0, 1, '2025-04-05 13:00:00',
        2, 1, 1, '2025-04-10 18:00:00', 'Rifa Abril', 45
    )

    crear_boleto(nuevo_boleto)
    leer_boletos()
    actualizar_nombre_rifa(1, "Rifa Abril Actualizada")
    leer_boletos()
    eliminar_boleto(1)
    leer_boletos()
