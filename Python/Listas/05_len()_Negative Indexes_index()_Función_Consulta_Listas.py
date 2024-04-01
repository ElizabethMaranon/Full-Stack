lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
cantidad_lista = len(lista)
print(f"""
len() -> longitud, cantidad elementos,
lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
cantidad_lista = len(lista)
print(cantidad_lista) -> {cantidad_lista}
print(len(lista)) -> {len(lista)} -> sin crear variable
-----""")
ultimo_elemento = lista[-1]
print(f"""Negative Indexes -> ultimo elmento de la lista
ultimo_elemento = lista[-1]
print(ultimo_elemento) -> {ultimo_elemento}
print(lista[-1]) {lista[-1]} sin crear variable
-----""")
index_ultimo_elemento = lista.index(ultimo_elemento)
print(f"""index -> buscar indice del elemento
index_ultimo_elemento = lista.index(ultimo_elemento)
print(index_ultimo_elemento) -> {index_ultimo_elemento}
print(lista.index(ultimo_elemento)) -> {lista.index(ultimo_elemento)} sin crear variable
-----""")
print(f"""index ultimo elemento en solo un proceso
print(lista.index(lista[-1])) ->{lista.index(lista[-1])}
-----""")