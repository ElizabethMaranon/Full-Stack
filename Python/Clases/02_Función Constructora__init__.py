"""Creamos la funcion"""
class Factura:
    def __init__(self, cliente, total):
        self.cliente = cliente
        self.total = total
    def formatter(self):
        return f'{self.cliente} debe: {self.total}€'
"""Creamos las instancias"""
Mielma = Factura('Mielmna', 100)
Developer = Factura('Developer', 200)
FullStack = Factura('FullStack', 150)
