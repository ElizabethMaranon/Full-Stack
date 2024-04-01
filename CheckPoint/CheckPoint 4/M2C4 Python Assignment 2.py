from decimal import Decimal
import math
print(f"""
Asignación de Python M2C4""")
print("""
Ejercicio 1: Cree una lista, tupla, flotante, entero, decimal y diccionario.
Para los decimales necesitamos importar la biblioteca -> from decimal import Decimal""")
lista = ['uno', 'dos', 'tres']
tupla = ('uno', 'dos', 'tres')
flotante = 1.23
entero = 1
decimal = Decimal(1.23)
diccionario = {'uno' : 'bat', 'dos' : 'bi', 'tres' : 'hiru'}
print(f"""
Importante diferenciar los corchetes de la lista[], tupla() y diccionario{{}}.
lista -> {lista} 
tupla -> {tupla}
flotante -> {flotante}
entero -> {entero}
decimal -> {decimal} 
diccionario -> {diccionario}
""")
print('-----')
print(f"""
Ejercicio 2: Redondea tu flotador.
Para las funciones matemáticas necesitamos importar la biblioteca -> import math

Redondeo hacia arriba, math.ceil -> {math.ceil(flotante)}
Redondeo hacia abajo, math.floor-> {math.floor(flotante)}
Redondeo al más cercano, round-> {round(flotante)}
""")
print('-----')
print(f"""
Ejercicio 3: Obtén la raíz cuadrada de tu flotador.

Función sqrt -> {math.sqrt(flotante)}
""")
print('-----')
print(f"""
Ejercicio 4: Seleccione el primer elemento de su diccionario.

Buscamos key para encontrar el valor{diccionario['uno']}
""")
print('-----')
print(f"""
Ejercicio 5: Seleccione el segundo elemento de su tupla.

Usamos index {tupla[1]}""")

print(f"""
Ejercicio 6: Añade un elemento al final de tu lista.
""")
lista.append('cuatro') 
print(f"""Función append -> {lista}""")
print("""
-----""")
print("""
Ejercicio 7: Reemplace el primer elemento de su lista.
""")
lista[0] = 'bat'
print(f"""Cambiamos el elemento mediante el index de la lista ->  {lista}""")
print("""
-----""")
print("""
Ejercicio 8: Ordena tu lista alfabéticamente.
""")
lista.sort()
print(f"""Función sort, orden a-z -> {lista}""")
lista.sort(reverse=True)
print(f"""Función sort(reverse=True), orden z-a-> {lista}""")
print("""
-----""")
print("""Ejercicio 9: Utilice la reasignación para agregar un elemento a su tupla.
Tupla inmutable. Reasignamos la variable""")
tupla += 'cuatro',
print(tupla)
print("""
-----""")