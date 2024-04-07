import math
lista = [100, 83, 220, 40, 100, 400, 10, 1, 3,]
sorted_lista = sorted(lista)
media = sorted_lista[(math.floor(len(sorted(lista))/2))]
print(f'''
Tools: math library, sorted function, list slicing, computations
lista = [100, 83, 220, 40, 100, 400, 10, 1, 3]
-----
Cantidad de elementos de la lista  
print(len(lista) -> {len(lista)}
-----
Ordenamos la lista en una nueva variable
sorted_lista = sorted(lista) -> {sorted_lista}
-----
Buscamos el valor bajo de la mitad cantidad de la lista
cantidad 9, mitad 4,5, valor bajo 4
print(math.floor(len(sorted_lista)/2) -> {math.floor(len(sorted(lista))/2)}
-----
Buscamos el valor obtenido como index,
index 4 sería el 5(numero central de 9)
media = sorted_lista[math.floor(len(sorted(lista))/2)] -> {media}
-----
En una sola linea
print(sorted(lista)[math.floor(len(sorted(lista))/2)]) -> {sorted(lista)[math.floor(len(sorted(lista))/2)]}
''')






