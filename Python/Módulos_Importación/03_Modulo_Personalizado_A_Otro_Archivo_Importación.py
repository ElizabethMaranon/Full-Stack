"""
Cuando la libreria esta en el mismo directorio"""
import Libreria_Mismo_Directorio

def Importada_Mismo_Directorio():
  print(Libreria_Mismo_Directorio.saludo('E', 'm'))
Importada_Mismo_Directorio()
"""Cuando la librería esta en otro directorio"""
import sys # importamos sistema
sys.path.insert(0, './Libreria') # importamos directorio
import Otro_Directorio

def Importada_Otro_Directorio():
  print(Otro_Directorio.agurra('e','m'))
Importada_Otro_Directorio()

