class Factura: 
    def __init__(self, cliente, total): #Creamos una función
        self._cliente = cliente # Asignamos argumentos al objeto, protegipo por _
        self._total = total # Asignamos argumentos al objeto, protegipo por _
    def formatter(self): # Función básica de formatter
        return f'{self._cliente} debe: {self._total}€' # ·devuelve una string con los datos
    @property # damos acceso leer aunque esté protegido
    def cliente(self):
        return self._cliente
    @cliente.setter # damos acceso cambio aunque esté protegido
    def cliente(self, cliente):
        self._cliente = cliente
    @property # damos acceso leer aunque esté protegido
    def total(self):
        return self._total
    
Mielma = Factura('Mielma', 100) # Creamos una instancia
print(Mielma.cliente) # Nos devuelve Mielma, tiene acceso gracias a property, sino da error de acceso
Mielma.cliente = 'Developer' # Nos devuelve Mielma, tiene acceso a cambio setter
print(Mielma.cliente)
"Mielma.total = 200" # AttributeError: property 'total' of 'Factura' object has no setter (no cambio)


print(Mielma.total) # Nos devuelve 100, tiene acceso gracias a property, sino da error de acceso

"ejercicio"

class Garage:
  def __init__(self, size):
    #   Protect the size attribute
    self._size = size # Con _ protegemos
    self.cars = []

  # add decorator here
  @property # Permiso lectura, pero no cambio
  def size(self):
        return self._size

  def open_door(self):
    return "The door opens"