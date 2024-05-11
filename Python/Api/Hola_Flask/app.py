from flask import Flask # Diferencia mayúsculas importar libreria

app = Flask(__name__) # Creamos variable, en este caso la más básica

@app.route('/') # Creamos la ruta de la variable @nombrevariable.reoute('directorio que')
def hola(): # Creamos la función
    return "Hey Flask" # Devuelve Hey Flask

if __name__== '__main__': # Condicion si el nombre es igual al principal
    app.run(debug=True) # Ejecutar aplicación 
    
    