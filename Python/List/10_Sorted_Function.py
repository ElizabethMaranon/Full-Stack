print('''
lista = [6, 0, 5, 2, 1, 4, 3]
-----''')
lista = [6, 0, 5, 2, 1, 4, 3]
print('''ordena y cambia la estructura de los elementos
lista.sort()''')
lista.sort()
print(lista)
print('''-----''')
print('''devuelve none, no devuelve valor
new_lista = lista.sort()
print(new_lista) ''')
lista = [6, 0, 5, 2, 1, 4, 3]
new_lista = lista.sort()
print(new_lista)
print('''-----''')
print('''sorted ->ordena en una nueva variable y no cambia la estructura de los elementos
sorted_lista = sorted(lista)
print(sorted_lista)
sorted_lista_reverse = sorted(lista, reverse=True)
print(sorted_lista_reverse)
print(lista) lista esta sin cambiar''')
lista = [6, 0, 5, 2, 1, 4, 3]
sorted_lista = sorted(lista)
sorted_lista_reverse = sorted(lista, reverse=True)
print(sorted_lista)
print(sorted_lista_reverse)
print(lista)
print('''-----''')
