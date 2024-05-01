class Factura: 
    def __init__(self, cliente, total): 
        self.cliente = cliente 
        self.total = total 
        
    def __str__(self):
        return f'La Factura de {self.cliente} asciende a {self.total} €'
    def __repr__(self):
        return f'La factura de <valor: cliente: {self.cliente}, total: {self.total}>'

fact = Factura('Mielma', 150)
print('')
print(str(fact))
print(repr(fact))
print('')
