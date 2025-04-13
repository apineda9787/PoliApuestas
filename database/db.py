import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Esta clase establece la conexión a las base de datos MySQL usando SQLAlchemy
# SQLAlchemy es un ORM (Object Relational Mapper) que permite interactuar con bases de datos de una manera más sencilla y orientada a objetos.

connection_string = "mysql+mysqlconnector://root:Thommy1945*@localhost:3306/poli_apuestas"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Esta clase es la base para todas las clases de modelo que se definan en el proyecto.
Base = declarative_base()