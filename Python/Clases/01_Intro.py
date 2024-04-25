"""Un método de instancia es un método que modifica o accede al estado del objeto al que hace referencia. Recibe self como primer parámetro, el cual se convierte en el propio objeto sobre el que estamos trabajando. Python envía este argumento de forma transparente: no hay que pasarlo como argumento."""
class Factura:
    def saludo(self):# obligaroio yo(self), se explicará mas adelante
        return('Hola')
    
fact_uno = Factura()

print(fact_uno)

"""imprime <__main__.Factura object at 0x0000016B613E5DF0>
__ se llama dumber, abreviatura de doble subrayado
factura object -> hemos creado una instancia de Factura
at 0x0000016B613E5DF0 -> Lugar de memoria de la computadora donde Python almacena esta factura
para que imprima, tenemos que llamar a la función"""

fact_dos = Factura()

print(fact_dos.saludo())