# Agregar las dependencias instaladas, Diferencia mayúsculas de minúsculas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__) # Crear variable, en este caso la más básica

@app.route('/') # Crear la ruta de la variable @nombrevariable.route('directorio')
def hola(): # Crear la función
    return "Hola Flask" # Devuelve "mensaje"

if __name__ == '__main__': # Condición si el nombre es igual al principal
    app.run(debug=True)  #Ejecutar aplicación
    
    