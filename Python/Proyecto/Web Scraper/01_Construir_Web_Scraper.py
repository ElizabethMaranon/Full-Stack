"""Web Scraper -> Ir a la web para extrar componentes que luego se pueden usar, cuando no se usa api"""
"""Comunicarse con API externas"""
"""Librería request para comunicar con api"""

"""Ejercicio
Programa que coje la url y luego saca el código
Seleccionar enlaces a los posts
hacer funcion que coga post y convertirlo en pagina"""
"""Pistas
Librería request
Librería inflection (averiguar que es)
Librería beautifulsoup (para scrapinkg)
pip install request
pip install inflection
pip install beautifulsoup4 # hay que poner la ultima version """

#https://es.kiosko.net/es/free.html
import requests
from bs4 import BeautifulSoup
from inflection import titleize

r = requests.get('https://es.kiosko.net/es/free.html')
#print(r.text)#para imprimir la pagina en formato texto

soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')#buscará todos los enlaces
#print(links)

for link in links:
    print(link['href']) 
print(link['href'])