# class Factura:
#     def __str__(self):
#         return 'Esta es la clase de Factura'

# fact = Factura()

# print(str(fact))

class Factura: 
    def __init__(self, cliente, total): 
        self.cliente = cliente 
        self.total = total 
        
    def __str__(self):
        return f'La Factura de {self.cliente} asciende a {self.total} €'

fact = Factura('Mielma', 150)

print(str(fact))

