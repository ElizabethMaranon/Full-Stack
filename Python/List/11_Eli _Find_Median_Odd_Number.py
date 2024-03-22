import math
print('''
Tools:
- math library
- sorted function
- list slicing
- computations
lista = [100, 83, 220, 40, 100, 400, 10, 1, 3]
-----''')
lista = [100, 83, 220, 40, 100, 400, 10, 1, 3,]
print('print(len(lista))')
print(len(lista))
print('sorted_lista = sorted(lista)')
sorted_lista = sorted(lista)
print(sorted_lista)
print('print(math.floor(len(sorted_lista)/2))')
print(math.floor(len(sorted(lista))/2))
print('media = sorted_lista[math.floor(len(sorted(lista))/2)]')
media = sorted_lista[(math.floor(len(sorted(lista))/2))]
print(media)
print('''-----''')
print(sorted(lista)[math.floor(len(sorted(lista))/2)])
