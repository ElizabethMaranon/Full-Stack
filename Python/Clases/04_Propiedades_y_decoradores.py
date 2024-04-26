class Factura: 
    def __init__(self, cliente, total): #Creamos una función
        self.cliente = cliente # Asignamos argumentos al objeto
        self.total = total # Asignamos argumentos al objeto
    def formatter(self): # Función básica de formatter
        return f'{self.cliente} debe: {self.total}€' # ·devuelve una string con los datos
    
Mielma = Factura('Mielma', 100) # Creamos una instancia

print(Mielma.cliente) # Nos devuelve Mielma
print(Mielma.total) # Nos devuelve 100

Mielma.cliente = 'Developer'
print(Mielma.cliente) # Nos devuelve Developer
