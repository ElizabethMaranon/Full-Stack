import fnmatch #libreria Coincidencia de patrones de nombre de archivos Unix
import os #librería sistema operativo 

def lista_archivos():
    for archivo in os.listdir('.'):
        if fnmatch.fnmatch(archivo, "*.txt"):
            print("Archivo Texto:, ", archivo)
        if fnmatch.fnmatch(archivo, "*.rb"):
            print("Archivo Ruby:, ", archivo)
        if fnmatch.fnmatch(archivo, "*.yml"):
            print("Archivo Yaml:, ", archivo)
        if fnmatch.fnmatch(archivo, "*.py"):
            print("Archivo Python:, ", archivo)
            
lista_archivos()
def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file)

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()