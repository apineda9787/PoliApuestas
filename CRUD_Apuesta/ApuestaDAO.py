from Conexion import conectar


def obtener_apuestas():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id_apuesta, id_usuario, id_deporte, id_campeonato, id_partido, valor_boleto, marcador_apuesta_primer_equipo, "
        "marcador_apuesta_segundo_equipo FROM apuesta;")
        apuestas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return apuestas
    return []


def crear_apuesta(id_usuario, id_deporte, id_campeonato, id_partido, valor_boleto, marcador1, marcador2):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = """INSERT INTO Apuesta (id_usuario, id_deporte, id_campeonato, id_partido, valor_boleto, 
        marcador_apuesta_primer_equipo, marcador_apuesta_segundo_equipo) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (id_usuario, id_deporte, id_campeonato, id_partido, valor_boleto, marcador1, marcador2)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Apuesta creada correctamente.")


def actualizar_apuesta(id_apuesta, valor_boleto, marcador1, marcador2):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = """UPDATE Apuesta 
                 SET valor_boleto = %s, marcador_apuesta_primer_equipo = %s, marcador_apuesta_segundo_equipo = %s 
                 WHERE id_apuesta = %s"""
        valores = (valor_boleto, marcador1, marcador2, id_apuesta)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Apuesta actualizada correctamente.")


def eliminar_apuesta(id_apuesta):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = "DELETE FROM Apuesta WHERE id_apuesta = %s"
        cursor.execute(sql, (id_apuesta,))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Apuesta eliminada correctamente.")
