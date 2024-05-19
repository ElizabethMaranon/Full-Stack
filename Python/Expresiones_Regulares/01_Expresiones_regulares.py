import fnmatch #biblioteca Coincidencia de patrones de nombre de archivos Unix
from fnmatch import fnmatchcase
import os #biblioteca sistema operativo 

def lista_archivos():
    for archivo in os.listdir('D:\Eli\Documents\Full-Stack\Python\Expresiones_Regulares'): #'.' misma carpeta
        if fnmatch.fnmatch(archivo, "*.txt"):
            print("Archivo Texto:, ", archivo)
        if fnmatch.fnmatch(archivo, "*.rb"):
            print("Archivo Ruby:, ", archivo)
        if fnmatch.fnmatch(archivo, "*.yml"):
            print("Archivo Yaml:, ", archivo)
        if fnmatch.fnmatch(archivo, "*.py"):
            print("Archivo Python:, ", archivo)
            
lista_archivos()

equipos = [ # Creamos lista que contenga los equipos y los goles marcados
    "Equipo X goles 1",
    "Equipo Z goles 2",
    "Equipo W goles 1",
    "Equipo K goles 1"
]

goles2 = [equipo for equipo in equipos if fnmatchcase(equipo, "* 2")] # For in para bucle de busqueda

print(goles2)