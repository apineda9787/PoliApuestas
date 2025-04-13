from database.db import session  # Usar la sesión ya creada
from sqlalchemy import Column, Integer, String, Float
from database.db import Base  # Asegurarse de que Base esté importado

class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)  # Eliminar autoincremento
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    saldo_disponible = Column(Float, nullable=False)

    def __init__(self, nombre, correo, contraseña, saldo_disponible, id_usuario=None):
        
        # Asegúrate de pasar id_usuario como un argumento opcional
        self.id_usuario = id_usuario  # Ahora acepta el id_usuario como parámetro opcional
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.saldo_disponible = saldo_disponible

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', correo='{self.correo}', saldo={self.saldo_disponible})>"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}