lista = [6, 0, 5, 2, 1, 4, 3]
print('''
lista = [6, 0, 5, 2, 1, 4, 3]
-----''')
lista.sort()
print(f"""ordena y cambia la estructura de los elementos
lista.sort()-> {lista}
-----""")
lista = [6, 0, 5, 2, 1, 4, 3]
orden_lista = lista.sort()
print(f"""devuelve none, no devuelve valor
orden_lista = lista.sort() -> {orden_lista}
-----""")
lista = [6, 0, 5, 2, 1, 4, 3]
ordenada_funcion = sorted(lista)
ordenada_funcion_reverse = sorted(lista, reverse=True)
print(f"""sorted -> ordena en una nueva variable y no cambia la estructura de los elementos
ordenada_funcion = sorted(lista)
print(ordenada_funcion) -> {ordenada_funcion}
ordenada_funcion_reverse = sorted(lista, reverse=True)
print(ordenada_funcion_reverse) -> {ordenada_funcion_reverse}
print(lista) -> {lista} -> está sin cambiar
-----""")