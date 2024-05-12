from dataclasses import fields
from flask import Flask # Agregamos las dependencias instaladas, Diferencia mayúsculas de minúsculas
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os # Librería del sistema operativo
from flask import Flask, request, jsonify # Agregamos librería

app = Flask(__name__) # Creamos variable, en este caso la más básica

directorio_base = os.path.abspath(os.path.dirname(__file__))# Ruta relativa # Devuelve primera parte ruta
# SQLALCHEMY_DATABASE_URI -> Cadena de conexión db. Crear db, pasar directorio y el nombre
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio_base, 'app.sqlite')
db = SQLAlchemy(app) # Crear objeto db.
ma = Marshmallow(app)# Trabajar con Marshmallow

# Esquema de las guías
class Guía(db.Model): #(Hereda modelo)
    id = db.Column(db.Integer, primary_key=True) # API cree un nuevo registro en la db-> db +1.
    título = db.Column(db.String(100), unique=False) # string(Número) Cantidad de caracteres
    contenido = db.Column(db.String(144), unique=False)

    def __init__(self, título, contenido): # Constructor, método init
        self.título = título
        self.contenido = contenido
        
# Schema
class GuíaEsquema(ma.Schema):
    class Meta:
        fields = ('título', 'contenido')
        
Guía_Esquema = GuíaEsquema() # Crear instancia trabajando con una guía
Guías_Esquema = GuíaEsquema(many=True) # Crear instancia trabajando con varias guías

@app.route('/guía', methods=["POST"]) # Primer punto final
def añadir_guía(): # Crear función añadir guía
    título = request.json['título'] # Almacenar en variable el valor del título
    contenido = request.json['contenido'] # Almacenar en variable el valor del contenido
    
    nueva_guía = Guía(título, contenido) # Crear instancia de nueva guía
    
    db.session.add(nueva_guía) # Comunicarse con db
    db.session.commit() # Confirmar
    
    guía = Guía.query # Realizar consulta
    
    return Guía_Esquema.jsonify(guía)

if __name__== '__main__': # Condición si el nombre es igual al principal
    app.run(debug=True) # Ejecutar aplicación
    

