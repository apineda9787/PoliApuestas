import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine = create_engine(mysql.connector.connect(user="root", password="1234", host="localhost", database="agenda", port="3306"))
connection_string = "mysql+mysqlconnector://root:Thommy1945*@localhost:3306/poli_apuestas"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()