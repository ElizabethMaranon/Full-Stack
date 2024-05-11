# Agregamos las dependencias instaladas, Diferencia mayúsculas de minúsculas
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__) # Creamos variable, en este caso la más básica

directorio_base = os.path.abspath(os.path.dirname(__file__))# Convertir una ruta relativa en una ruta absoluta

if __name__== '__main__': # Condición si el nombre es igual al principal
    app.run(debug=True) # Ejecutar aplicación 

