import db
from sqlalchemy import Column, Integer, String, Float

class Usuario(db.Base):
    __tablename__ = 'usuario'  # Debe coincidir con la tabla en la BD

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    saldo_disponible = Column(Float, nullable=False)

    def __init__(self, nombre, correo, contraseña, saldo_disponible):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.saldo_disponible = saldo_disponible

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', correo='{self.correo}', saldo={self.saldo_disponible})>"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
