"""
Cuando solo vamos a necesitar una función, sin necesidad del resto de biblioteca
"""
from biblioteca_Mismo_Directorio import saludo

def Saludo():
  print(saludo('Mielma', 'Developer'))
  
Saludo()
print('-----')
import sys
sys.path.insert(0, './biblioteca Mielma')
from Otro_Directorio import agurra

def Agurra():
  print(agurra('Mielma', 'Developer'))

Agurra()

