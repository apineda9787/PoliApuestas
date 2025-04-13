import sys
import os
import database.db as db
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database')))

from flask import Flask, jsonify, request
from sqlalchemy import text
from typing import Optional
from model.Usuario import Usuario

app = Flask(__name__)

# Bloque de prueba para verificar la conexión a la base de datos
try:
    db.session.execute(text('SELECT 1'))
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print("Error al conectar a la base de datos:", e)
    exit(1)  # Termina la ejecución si la conexión falla

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

if __name__ == '__main__':
    # Crear las tablas si no existen
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True, port=5000)