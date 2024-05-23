
class Música: # Creamos una clase
    def __init__(self, cantante, album): #Creamos una función
        self.cantante = cantante # Asignamos argumentos al objeto
        self.album = album # Asignamos argumentos al objeto
    def formatter(self): # Función básica de formatter
        return f'El último album de {self.cantante} se titula {self.album}' # devuelve una string con los datos
    
"""Creamos las instancias"""

Saurom = Música('Saurom', 'Pájaro Fantasma')
Debler = Música('Debler Eternia', 'Perverso')
Lepoka = Música('Lepoka', 'El baile de los caídos')

print(Saurom.formatter())
print(Debler.formatter())
print(Lepoka.formatter())

"Ejercicio"
class Garage:
  def __init__(self, size):
      self.size = size

  def open_door(self):
    return "The door opens"
    
home = Garage(2) # instantiate with a garage size here

print(home.open_door())