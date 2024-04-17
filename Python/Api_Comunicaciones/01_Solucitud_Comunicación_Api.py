"""
Instalar -> Abrir terminal -> pip install requests
pprint deberia de estar en el sistema, sino instalar mediante pip
"""
import requests
import pprint
r = requests.get('https://api.dailysmarty.com/posts')
r.json()
pprint.pprint(r.json()['posts'][0]) #paquete.funcion(var.json['diccionario key'][index, desde ultimo post])
pprint.pprint(r.json()['posts'][0]['url_for_post']) #[Para obtener la url]