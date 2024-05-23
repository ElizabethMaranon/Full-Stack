"""
API -> application programming interface (Interfaz de Programación de Aplicaciones)
Lenguaje que usa nuestra aplicación para comunicarse con otras aplicaciones
Instalar -> Abrir terminal -> pip install requests
pprint debería de estar en el sistema, sino instalar mediante pip install pprintpp
"""

import requests
import pprint

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

r.json()
# paquete.funcion(var.json['diccionario key'][index, desde ultimo post])
pprint.pprint(r.json()['abilities'][1]) 
#[Para obtener la url]
pprint.pprint(r.json()['abilities'][1]['ability']['url']) 

