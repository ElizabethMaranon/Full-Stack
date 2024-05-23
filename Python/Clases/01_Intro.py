class saludo: # Crear clase
    def presentación(self):# Crear presentación, obligatorio yo(self)
        return('Hola, soy Mielma') # Crear retorno
    
instancia = saludo() # Creamos variable

print(instancia)
"""imprime <__main__.saludo object at 0x000002093AC77500>

__ se llama dumber, abreviatura de doble subrayado

factura object -> hemos creado una instancia de presentación

at 0x0000016B613E5DF0 -> Lugar de memoria de la computadora donde Python almacena esta factura"""

print(instancia.presentación())



"Ejercicio"
class Garage:
    def open_door(self):
        return("The door opens")
home = Garage()

print(home.open_door())