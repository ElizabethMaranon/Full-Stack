
". "
""
"El proceso que les voy a mostrar aquí puede estar mal visto porque les brinda demasiado acceso y esencialmente les permite hacer cualquier cosa que quieran."

class Factura: # Creamos una clase
    def __init__(self, cliente, total): #Creamos una función
        self.cliente = cliente # Asignamos argumentos al objeto
        self.total = total # Asignamos argumentos al objeto
    def formatter(self): # Función básica de formatter
        return f'{self.cliente} debe: {self.total}€' # ·devuelve una string con los datos
    
"""Creamos las instancias"""
Mielma = Factura('Mielma', 100)

"Accedemos al valor del cliente,  porque se guardó como objeto"
print(Mielma.cliente) # Nos devuelve Mielma
print(Mielma.total) # Nos devuelve 100

"""Podemos crear valores una vez creado todo el objeto, en otros lenguajes se llama proceso establecedor
donde pudimos ingresar al objeto
y luego establecer un valor. Por lo general, solo podía establecer el valor cuando creaba la clase y luego, si desea cambiarlo o anular un valor, necesitaba crear una función de establecimiento,"""
Mielma.cliente = 'Developer'
print(Mielma.cliente) # Nos devuelve Developer


"Coding Exercise"
"""Hemos agregado una variedad de autos a nuestro garaje.
Todos los vehículos están fuera por el día y necesitamos actualizar el conjunto.
Use un definidor para actualizar la matriz de autos para reflejar todos los autos que desaparecieron.
Entonces, en el get_cars variable, obtenga los datos de los autos del home objeto."""


# Starter code
class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
# End of starter code

class Garage:
  def __init__(self,out):
    self.out = out
    self.cars = ["Ram", "Model 3"]

  def formatter(self): 
        return f'{self.cars}'
get_cars = Garage(0)
print(get_cars.cars)