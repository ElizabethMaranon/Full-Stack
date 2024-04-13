"""
Cuando solo vamos a necesitar una función, sin necesidad del resto de librería

Desde Libreria_Mismo_Directorio importar saludo ->
from Libreria_Mismo_Directorio import saludo
Al haber importado sólo la función, para imprimir, llamar solo función->
print(saludo('Mielma', 'Developer'))

Desde Libreria_Mismo_Directorio importar agurra
import sys
sys.path.insert(0, './Libreria')
from Libreria_Mismo_Directorio import agurra

print(agurra('Mielma', 'Developer'))

"""
from Libreria_Mismo_Directorio import saludo

def Saludo():
  print(saludo('Mielma', 'Developer'))
  
Saludo()

import sys
sys.path.insert(0, './libreria')
from Otro_Directorio import agurra

def Agurra():
  print(agurra('Mielma', 'Developer'))

Agurra()

