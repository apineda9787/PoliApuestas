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
def crear_boleto(data):
    try:
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
    except IntegrityError as e:
        print("❌ Error de integridad: asegúrate de que los IDs relacionados (como id_apuesta) existan.")
        print(f"🔎 Detalle: {e}")
    except Error as e:
        print(f"❌ Error general al crear el boleto: {e}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()

# READ
def leer_boletos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Boleto")
        resultados = cursor.fetchall()
        if resultados:
            headers = [desc[0] for desc in cursor.description]
            print(tabulate(resultados, headers=headers, tablefmt="grid"))
        else:
            print("⚠️ No hay boletos registrados.")
    except Error as e:
        print(f"❌ Error al leer boletos: {e}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()

# UPDATE
def actualizar_nombre_rifa(id_boleto, nuevo_nombre_rifa):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "UPDATE Boleto SET nombre_rifa = %s WHERE id_boleto = %s"
        cursor.execute(sql, (nuevo_nombre_rifa, id_boleto))
        conexion.commit()
        if cursor.rowcount > 0:
            print("✏️ Nombre de la rifa actualizado.")
        else:
            print("⚠️ No se encontró un boleto con ese ID.")
    except Error as e:
        print(f"❌ Error al actualizar: {e}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()

# DELETE
def eliminar_boleto(id_boleto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "DELETE FROM Boleto WHERE id_boleto = %s"
        cursor.execute(sql, (id_boleto,))
        conexion.commit()
        if cursor.rowcount > 0:
            print("🗑️ Boleto eliminado.")
        else:
            print("⚠️ No se encontró un boleto con ese ID.")
    except Error as e:
        print(f"❌ Error al eliminar: {e}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()