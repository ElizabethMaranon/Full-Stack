class Web:
    def __init__(self, título): # Init dunder constructor
        self.título = título # Valor del atributo de instancia

wb = Web('Mielma web') # Creamos instancia 
print(wb.título) # Imprimimos

print(wb.__dict__) # Convierte en dicccionario, muestra los atributos y sus valores

class Web2: # No tiene constructor
    título = 'Mielma web2' # Creamos variable, atributo de clase
    
wb2 = Web2() # Creamos instancia,
print(wb2.__dict__) # No obtenemos ningún atributo
print(wb2.título) # Imnprimimos título

    