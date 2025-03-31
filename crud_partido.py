import mysql.connector

def get_connection():
    """Establece conexión con la base de datos."""
    try:
        conn = mysql.connector.connect(
            user='root',
            password='123456', 
            host='localhost',
            database='PoliApuestas',
            port='3306'
        )
        print("Conexión exitosa a la base de datos")
        return conn
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def verificar_id_deporte(id_deporte):
    """Verifica si el id_deporte existe en la tabla Deporte."""
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id_deporte FROM Deporte WHERE id_deporte = %s", (id_deporte,))
            resultado = cursor.fetchone()
        conn.close()
        return resultado is not None
    return False

def crear_partido(id_deporte, fecha_hora_partido, equipo1, equipo2, marcador1, marcador2, min_apuesta, max_apuesta):
    """Inserta un nuevo partido en la base de datos."""
    if not verificar_id_deporte(id_deporte):
        print(f"Error: El id_deporte {id_deporte} no existe en la tabla Deporte.")
        return
    
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO Partido (id_deporte, fecha_hora_partido, nombre_equipo_1, nombre_equipo_2, marcador_equipo_1, marcador_equipo_2, monto_minimo_apuesta, monto_maximo_apuesta)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (id_deporte, fecha_hora_partido, equipo1, equipo2, marcador1, marcador2, min_apuesta, max_apuesta)
                cursor.execute(query, valores)
                conn.commit()
                print(" Partido creado exitosamente")
        except mysql.connector.Error as e:
            print(f"Error al crear el partido: {e}")
        finally:
            conn.close()

def leer_partidos():
    """Muestra todos los partidos registrados en la base de datos."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Partido")
                partidos = cursor.fetchall()
                for partido in partidos:
                    print(partido)
        except mysql.connector.Error as e:
            print(f"Error al leer los partidos: {e}")
        finally:
            conn.close()

def actualizar_partido(id_partido, nuevo_equipo1, nuevo_equipo2):
    """Actualiza los nombres de los equipos en un partido."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                query = """
                    UPDATE Partido
                    SET nombre_equipo_1 = %s, nombre_equipo_2 = %s
                    WHERE id_partido = %s
                """
                cursor.execute(query, (nuevo_equipo1, nuevo_equipo2, id_partido))
                conn.commit()
                print("Partido actualizado exitosamente")
        except mysql.connector.Error as e:
            print(f"Error al actualizar el partido: {e}")
        finally:
            conn.close()

def eliminar_partido(id_partido):
    """Elimina un partido por su ID."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Partido WHERE id_partido = %s", (id_partido,))
                conn.commit()
                print("Partido eliminado exitosamente")
        except mysql.connector.Error as e:
            print(f"Error al eliminar el partido: {e}")
        finally:
            conn.close()

def mostrar_bases_de_datos():
    """Muestra todas las bases de datos disponibles en MySQL."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SHOW DATABASES")
                for base in cursor.fetchall():
                    print(base)
        except mysql.connector.Error as e:
            print(f"Error al mostrar las bases de datos: {e}")
        finally:
            conn.close()

# Ejemplos de uso
def main():
    crear_partido(1, '2025-03-21 18:00:00', 'Equipo A', 'Equipo B', 2, 1, 1000.0, 5000.0)
    leer_partidos()
    actualizar_partido(1, 'Nuevo Equipo A', 'Nuevo Equipo B')
    eliminar_partido(1)
    mostrar_bases_de_datos()

if __name__ == "__main__":
    main()