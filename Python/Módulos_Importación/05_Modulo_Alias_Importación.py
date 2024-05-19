"""Importar la biblioteca y crear función"""
import sys
sys.path.insert(0, './biblioteca Mielma')
import Otro_Directorio as Otro #as alias, para acortar nombre

def Agurra():
  print(Otro.agurra('Mielma', 'Developer'))

Agurra()