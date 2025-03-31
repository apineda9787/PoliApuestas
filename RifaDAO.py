import mysql.connector

# This function is used to connect to the database and return the connection object.
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
    
#This function is used to close the database connection.
def unconnection(conn):
    if conn:
        conn.close()

def findAll():
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rifa")
    rifas = cursor.fetchall()
    
    for rifas in rifas:
        print(rifas)
    
    unconnection(conn)

def crear_rifa(id_boleto, valor_boleto, fecha_ejecucion_sorteo, numero_aleatorio_ganador,
                   nombre_rifa, fecha_inicio, fecha_fin_rifa, premio_principal, premio_secundario,
                   premio_terciario, numero_max_participantes, numero_seleccionado_rifa):
    conn = getConnection()
    if not conn:
        return
    
    cursor = conn.cursor()
    rifaInsert = """INSERT INTO rifa (id_boleto, valor_boleto, fecha_ejecucion_sorteo, numero_aleatorio_ganador, 
                                 nombre_rifa, fecha_inicio, fecha_fin_rifa, premio_principal, premio_secundario, 
                                 premio_terciario, numero_max_participantes, numero_seleccionado_rifa) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    val = (id_boleto, valor_boleto, fecha_ejecucion_sorteo, numero_aleatorio_ganador, nombre_rifa,
                       fecha_inicio, fecha_fin_rifa, premio_principal, premio_secundario, premio_terciario,
                       numero_max_participantes, numero_seleccionado_rifa)
    print
    cursor.execute(rifaInsert, val)
    conn.commit()
    print(cursor.rowcount, "Rifa creada exitosamente.")
    unconnection(conn)

def obtener_rifa_por_id(id_rifa):
    conn = getConnection()
    if not conn:
        return

    cursor = conn.cursor()
    query = "SELECT * FROM rifa WHERE id_rifa = %s"
    val = (id_rifa,)

    cursor.execute(query, val)
    rifa = cursor.fetchone()
    
    if rifa:
        print(rifa)
    else:
        print("No se encontró la rifa con ID:", id_rifa)
    
    unconnection(conn)

def actualizar_rifa(self, id_rifa, **kwargs):
        try:
            cursor = self.conn.cursor()
            set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            valores = list(kwargs.values()) + [id_rifa]
            query = f"""
                UPDATE Rifa SET {set_clause} WHERE id_rifa = %s
            """
            cursor.execute(query, valores)
            self.conn.commit()
            print("Rifa actualizada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar rifa: {err}")


def eliminar_rifa(self, id_rifa):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM Rifa WHERE id_rifa = %s"
            cursor.execute(query, (id_rifa,))
            self.conn.commit()
            print("Rifa eliminada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar rifa: {err}")