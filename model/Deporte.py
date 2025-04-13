from database.db import session  # Usar la sesión ya creada
from sqlalchemy import Column, Integer, String, Float
from database.db import Base  # Asegurarse de que Base esté importado

class Deporte(Base):
    __tablename__ = 'deporte'

    id_deporte = Column(Integer, primary_key=True)
    nombre_deporte = Column(String(100), nullable=False)

    def __init__(self, id_deporte, nombre_deporte):
        self.id_deporte = id_deporte
        self.nombre_deporte = nombre_deporte

    def __repr__(self):
        return f"<Deporte(nombre_deporte='{self.nombre_deporte}')>"
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}