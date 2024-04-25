
class Factura: # Creamos una clase
    def __init__(self, cliente, total): #Creamos una función
        self.cliente = cliente # Asignamos argumentos al objeto
        self.total = total # Asignamos argumentos al objeto
    def formatter(self): # Función básica de formatter
        return f'{self.cliente} debe: {self.total}€' # ·devuelve una string con los datos
    
"""Creamos las instancias"""

Mielma = Factura('Mielma', 100)
Developer = Factura('Developer', 200)
FullStack = Factura('FullStack', 150)

print(Mielma.formatter())
print(FullStack.formatter())
print(Developer.formatter())

"Ejercicio"
class Garage:
  def __init__(self, size):
      self.size = size

  def open_door(self):
    return "The door opens"
    
home = Garage(2) # instantiate with a garage size here

print(home.open_door())