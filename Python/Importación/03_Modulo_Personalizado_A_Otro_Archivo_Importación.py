"""
Cuando la libreria esta en el mismo directorio"""
import Libreria_Mismo_Directorio

def Importada():
  print(Libreria_Mismo_Directorio.saludo('E', 'm'))

Importada()
"""Cuando la librería esta en otro directorio"""
import sys # importamos sistema
sys.path.insert(0, './Libreria') # importamos directorio
import Otro_Directorio

def Importada():
  print(Otro_Directorio.agurra('e','m'))
Importada()

