"""
API -> application programming interface (Interfaz de Programación de Aplicaciones)
Lenguaje que usa nuestra aplicación para comunicarse con otras aplicaciones
Instalar -> Abrir terminal -> pip install requests
pprint deberia de estar en el sistema, sino instalar mediante pip install pprintpp
"""

import requests
import pprint

r = requests.get('https://pokeapi.co/posts')

r.json()
pprint.pprint(r.json()['posts'][0]) 
pprint.pprint(r.json()['posts'][0]['url_for_post']) 