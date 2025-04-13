from database.db import session  # Session to interact with the database
from sqlalchemy import Column, Integer, String, Float # Import the necessary types for the columns
from database.db import Base # Base class for the models

# This class represents the 'usuario' table in the database.
class Usuario(Base):
    __tablename__ = 'usuario'

    # Define the columns of the table
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    saldo_disponible = Column(Float, nullable=False)

    # Constructor to initialize the object
    def __init__(self, nombre, correo, contraseña, saldo_disponible, id_usuario=None):
        
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.saldo_disponible = saldo_disponible

    # Method to represent the object as a string
    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', correo='{self.correo}', saldo={self.saldo_disponible})>"

    # Method to convert the object Usuario, to a dictionary
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}