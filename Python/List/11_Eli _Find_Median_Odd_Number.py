import math
print('''
Tools:
- math library
- sorted function
- list slicing
- computations
lista = [600, 500, 200, 100, 400, 300, 800, 700, 900]
-----''')
lista = [600, 500, 200, 100, 400, 300, 800, 700, 900]
'''print('print(len(lista))')
print(len(lista))
print('sorted_lista = sorted(lista)')
sorted_lista = sorted(lista)
print(sorted_lista)
print('print(math.ceil(len(sorted_lista)/2))')
print(math.ceil(len(sorted(lista))/2))
print('media = sorted_lista[math.ceil(len(sorted(lista))/2)]')
media = sorted_lista[math.ceil(len(sorted(lista))/2)]
print(media)'''
print('''-----''')
print(sorted(lista)[math.ceil(len(sorted(lista))/2)])
