# Agregar las dependencias instaladas, Diferencia mayúsculas de minúsculas
from flask import Flask, request, jsonify # Agregar biblioteca
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

# Punto final POST API en Flask
@app.route('/guía', methods=["POST"]) # Primer punto final
def añadir_guía(): # Crear función nueva guía
    título = request.json['título'] # Almacenar en variable valor título
    contenido = request.json['contenido'] # Almacenar en variable valor contenido
    
    nueva_guía = Guía(título, contenido) # Crear instancia de nueva guía
    
    db.session.add(nueva_guía) # comunicarse con db
    db.session.commit() # Confirmar
    
    guía = Guía.query.get(nueva_guía.id)
    
    return guía_esquema.jsonify(guía)

# Punto final todas las guías
@app.route("/guías", methods=["GET"]) # Punto final
def get_guías(): # Crear función
    todas_guías = Guía.query.all() # Almacenar en variable 
    resultado = guías_esquema.dump(todas_guías) # Uso esquema guía multiple
    return jsonify(resultado)

# Punto final para consultar una única guía
@app.route("/guía/<id>", methods=["GET"]) # Punto final # <id> Flask atento a ruta donde comienza guía
def get_guía(id): # Crear función
    guía = Guía.query.get(id) # Almacenar variable
    return guía_esquema.jsonify(guía) # Uso esquema guía única

# Punto final PUT Actualización guía
@app.route("/guía/<id>", methods=["PUT"]) # Punto final
def guía_update(id): # Crear función
    guía = Guía.query.get(id) # Almacenar variable
    título = request.json['título'] # Almacenar variable
    contenido = request.json['contenido'] # Almacenar variable
    
    guía.título = título 
    guía.contenido = contenido

    db.session.commit()
    return guía_esquema.jsonify(guía)# Uso esquema guía única

# Punto final Delete Eliminar registros
@app.route("/guía/<id>", methods=["DELETE"]) # Punto final
def guía_delete(id): # Crear función
    guía = Guía.query.get(id) # Almacenar variable
  
    db.session.delete(guía) # Comunicarse con db
    db.session.commit() # Confirmar

    # return guía_esquema.jsonify(guía) # Uso esquema guía única
    return "Guía eliminada correctamente" # Devuelve string
    
if __name__ == '__main__': # Condición si el nombre es igual al principal
    app.run(debug=True)  #Ejecutar aplicación
    
    