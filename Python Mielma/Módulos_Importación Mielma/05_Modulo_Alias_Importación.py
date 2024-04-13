"""Importar la librería y crear función"""
import sys
sys.path.insert(0, './Libreria Mielma')
import Otro_Directorio as Otro #as alias, para acortar nombre

def Agurra():
  print(Otro.agurra('Mielma', 'Developer'))

Agurra()