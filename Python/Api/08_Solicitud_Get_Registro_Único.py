# Agregar las dependencias instaladas, Diferencia mayúsculas de minúsculas
from flask import Flask, request, jsonify # Agregar librería
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__) # Crear variable, en este caso la más básica

basedir = os.path.abspath(os.path.dirname(__file__)) # Ruta relativa # Devuelve primera parte ruta
# SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app) # Crear objeto db
ma = Marshmallow(app) # Trabajar con Marshmallow

# Esquema de las guías
class Guía(db.Model): # Hereda modelo
    id = db.Column(db.Integer, primary_key=True) # Crear id, será la primary key
    título = db.Column(db.String(144), unique=False) # String(número) Cantidad de caracteres
    contenido = db.Column(db.String(144), unique=False)
    
    def __init__(self, título, contenido): # Constructor, método init
        self.título = título
        self.contenido = contenido

# Schema
class GuíaEsquema(ma.Schema):
    class Meta:
        fields = ('título', 'contenido')

guía_esquema = GuíaEsquema() # Crear instancia trabajando con una guía
guías_esquema = GuíaEsquema(many=True) # Crear instancia trabajando con varias guías   

# Crear punto final POST API en Flask
@app.route('/guía', methods=["POST"]) # Primer punto final
def añadir_guía(): # Crear función nueva guía
    título = request.json['título'] # Almacenar en variable valor título
    contenido = request.json['contenido'] # Almacenar en variable valor contenido
    
    nueva_guía = Guía(título, contenido) # Crear instancia de nueva guía
    
    db.session.add(nueva_guía) # comunicarse con db
    db.session.commit() # Confirmar
    
    guía = Guía.query.get(nueva_guía.id)
    
    return guía_esquema.jsonify(guía)

# Crear punto final todas las guías
@app.route("/guías", methods=["GET"]) # Punto final
def get_guías(): # Crear función
    todas_guías = Guía.query.all() # Almacenar en variable 
    resultado = guías_esquema.dump(todas_guías) # Uso esquema guía multiple
    return jsonify(resultado)

# Punto final para consultar una única guía
@app.route("/Guía/<id>", methods=["GET"]) # Punto final # <id> Flask atento a ruta donde comienza guía
def get_guía(id): # Crear función
    guía = Guía.query.get(id) # Almacenar variable
    return guía_esquema.jsonify(guía) # Uso esquema guía única

    

    
if __name__ == '__main__': # Condición si el nombre es igual al principal
    app.run(debug=True)  #Ejecutar aplicación
    
    