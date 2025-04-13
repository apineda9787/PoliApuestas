import sys
import os
import database.db as db
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database')))

from flask import Flask, jsonify, request
from sqlalchemy import text
from typing import Optional

from model.Deporte import Deporte
from model.Usuario import Usuario

# Esta es la configuración de Flask y la conexión a la base de datos.
app = Flask(__name__)

# Bloque de prueba para verificar la conexión a la base de datos
try:
    db.session.execute(text('SELECT 1'))
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print("Error al conectar a la base de datos:", e)
    exit(1)  # Termina la ejecución si la conexión falla

# ================== CRUD DE USUARIO ==================
# Obtener todos los usuarios de la base de datos.
@app.route('/getUsers', methods=['GET'])
def get_usuarios():
    usuarios = db.session.query(Usuario).all()
    usuarios_dict = [u.to_dict() for u in usuarios]
    return jsonify(usuarios_dict), 200

# Crear un nuevo usuario
@app.route('/createUser', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    try:
        nuevo_usuario = Usuario(
            id_usuario=data['id_usuario'],
            nombre=data['nombre'],
            correo=data['correo'],
            contraseña=data['contraseña'],
            saldo_disponible=float(data['saldo_disponible'])
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario creado', 'id': nuevo_usuario.id_usuario}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Actualizar usuario (id_usuario en el body)
@app.route('/updateUser', methods=['PUT'])
def actualizar_usuario():
    data = request.get_json()
    id_usuario = data.get('id_usuario')

    if not id_usuario:
        return jsonify({'error': 'El id_usuario es requerido'}), 400

    usuario = db.session.query(Usuario).get(id_usuario)
    if usuario:
        usuario.nombre = data.get('nombre', usuario.nombre)
        usuario.correo = data.get('correo', usuario.correo)
        usuario.contraseña = data.get('contraseña', usuario.contraseña)
        usuario.saldo_disponible = float(data.get('saldo_disponible', usuario.saldo_disponible))
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado'}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

# Eliminar usuario (id_usuario en el body)
@app.route('/deleteUser', methods=['DELETE'])
def eliminar_usuario():
    data = request.get_json()
    id_usuario = data.get('id_usuario')

    if not id_usuario:
        return jsonify({'error': 'El id_usuario es requerido'}), 400

    usuario = db.session.query(Usuario).get(id_usuario)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado'}), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

# ================= CRUD DE DEPORTE ==================

# Obtener todos los deportes de la base de datos.
@app.route('/getSports', methods=['GET'])
def get_deportes():
    deportes = db.session.query(Deporte).all()
    deportes_dict = [d.to_dict() for d in deportes]
    return jsonify(deportes_dict), 200

# Crear un nuevo deporte
@app.route('/createSport', methods=['POST'])
def crear_deporte():
    data = request.get_json()
    try:
        nuevo_deporte = Deporte(
            id_deporte=data['id_deporte'],
            nombre_deporte=data['nombre_deporte']
        )
        db.session.add(nuevo_deporte)
        db.session.commit()
        return jsonify({'message': 'Deporte creado', 'id': nuevo_deporte.id_deporte}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
# Actualizar deporte (id_deporte en el body)
@app.route('/updateSport', methods=['PUT'])
def actualizar_deporte():
    data = request.get_json()
    id_deporte = data.get('id_deporte')

    if not id_deporte:
        return jsonify({'error': 'El id_deporte es requerido'}), 400

    deporte = db.session.query(Deporte).get(id_deporte)
    if deporte:
        deporte.nombre_deporte = data.get('nombre_deporte', deporte.nombre_deporte)
        db.session.commit()
        return jsonify({'message': 'Deporte actualizado'}), 200
    else:
        return jsonify({'error': 'Deporte no encontrado'}), 404

# Eliminar deporte (id_deporte en el body)
@app.route('/deleteSport', methods=['DELETE'])
def eliminar_deporte():
    data = request.get_json()
    id_deporte = data.get('id_deporte')

    if not id_deporte:
        return jsonify({'error': 'El id_deporte es requerido'}), 400

    deporte = db.session.query(Deporte).get(id_deporte)
    if deporte:
        db.session.delete(deporte)
        db.session.commit()
        return jsonify({'message': 'Deporte eliminado'}), 200
    else:
        return jsonify({'error': 'Deporte no encontrado'}), 404


# ================= Inicio de la aplicación =================

if __name__ == '__main__':
    # Crear las tablas si no existen
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True, port=5000)