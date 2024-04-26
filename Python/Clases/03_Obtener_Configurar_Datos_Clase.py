"funciones captadoras"
"funciones establecidas"
"No hay que crear las fucniones, Python lo hace por tí"
"trabajar con propiedades y eso le permite tener control sobre qué datos puede anular y a qué datos tiene acceso en su objeto. "
"Esto no es posible en la mayoria de los lenguajes de programación"
"El proceso que les voy a mostrar aquí puede estar mal visto porque les brinda demasiado acceso y esencialmente les permite hacer cualquier cosa que quieran."
class Factura: # Creamos una clase
    def __init__(self, cliente, total): #Creamos una función
        self.cliente = cliente # Asignamos argumentos al objeto
        self.total = total # Asignamos argumentos al objeto
    def formatter(self): # Función básica de formatter
        return f'{self.cliente} debe: {self.total}€' # ·devuelve una string con los datos
    
"Creamos una instancia y accedemos al valor porque se guardó como objeto"
Mielma = Factura('Mielma', 100) # Creamos una instancia

print(Mielma.cliente) # Nos devuelve Mielma
print(Mielma.total) # Nos devuelve 100

"""Podemos crear valores una vez creado todo el objeto, en otros lenguajes se llama proceso establecedor,
donde pudimos ingresar al objeto y luego establecer un valor.
Por lo general, solo se puede establecer el valor cuando creas la clase y luego,
si desea cambiar o anular un valor, necesitas crear una función de establecimiento"""
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

# Setter goes here
home.cars = [] # Variable = matriz vacía que se va a ir actualizando

# Getter goes here
get_cars = home.cars

#imprimimos
print(get_cars)


get_cars = home(0)
print(get_cars.cars)