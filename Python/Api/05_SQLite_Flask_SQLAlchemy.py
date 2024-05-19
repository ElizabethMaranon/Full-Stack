# Agregar las dependencias instaladas, Diferencia mayúsculas de minúsculas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__) # Crear variable, en este caso la más básica

directorio = os.path.abspath(os.path.dirname(__file__)) # Ruta relativa # Devuelve primera parte ruta
# SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'app.sqlite')
db = SQLAlchemy(app) # Crear objeto db
ma = Marshmallow(app) # Trabajar con Marshmallow

# Esquema de las guías
class Guía(db.Model): # Hereda modelo
    id = db.Column(db.Integer, primary_key=True) # Api crea nuevo registro en la db: db +1
    título = db.Column(db.String(144), unique=False) # String(número) Cantidad de caracteres
    contenido = db.Column(db.String(144), unique=False)
    
    def __init__(self, título, contenido): # Constructor, método init
        self.título = título
        self.contenido = contenido

# Schema
class Guía_Esquema(ma.Schema):
    class Meta:
        fields = ('título', 'contenido')

guía_esquema = Guía_Esquema() # Crear instancia trabajando con una guía
guías_esquema = Guía_Esquema(many=True) # Crear instancia trabajando con varias guías   
    
if __name__ == '__main__': # Condición si el nombre es igual al principal
    app.run(debug=True)  #Ejecutar aplicación
    
    