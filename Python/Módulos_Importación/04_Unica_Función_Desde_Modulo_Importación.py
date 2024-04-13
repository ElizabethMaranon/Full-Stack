"""
Cuando solo vamos a necesitar una función, sin necesidad del resto de librería
"""
from Libreria_Mismo_Directorio import saludo

def Saludo():
  print(saludo('Mielma', 'Developer'))
  
Saludo()
print('-----')
import sys
sys.path.insert(0, './Libreria Mielma')
from Otro_Directorio import agurra

def Agurra():
  print(agurra('Mielma', 'Developer'))

Agurra()

