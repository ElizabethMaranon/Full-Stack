import math
print(
"""
Tools:
- math library
- sorted function
- list slicing
- computations
lista = [100, 83, 220, 40, 100, 400, 10, 1, 3]
-----""")
lista = [100, 83, 220, 40, 100, 400, 10, 1, 3]
sorted_lista = sorted(lista)
print(sorted_lista)
cantidad = len(sorted_lista)
print('cantidad = len(sorted_lista)')
print(cantidad)
mediana = sorted_lista[math.floor(cantidad/2):math.floor(cantidad/2)+1]
print('mediana = sorted_lista[:math.floor(cantidad/2):math.floor(cantidad/2) + 1]')
print(mediana)


print(''' mitad de listas, no es del ejercicio''')
primeros = sorted_lista[:math.floor(cantidad/2)]
print('''primeros = sorted_lista[:math.floor(cantidad/2)]
:math.floor -> elimina el primer valor para dejar par
(cantidad/2) divide entre dos''')
print(primeros)
print('ultimos = sorted_lista[-(math.floor(cantidad/2)):]')
ultimos = sorted_lista[-(math.floor(cantidad/2)):]
print(ultimos)



