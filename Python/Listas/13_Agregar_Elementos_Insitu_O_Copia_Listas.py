lista = ['cero', 'uno', 'dos', 'tres']
print(f"""
Agregar a lista existente y añadir elementos adicionales al final
lista = ['cero', 'uno', 'dos', 'tres']
-----""")
lista [-1] = 'sobreescribe'
print(f"""Sobreescribe elemento final, modifica lista
lista [-1] = 'sobreescribe -> {lista}
-----""")
lista.extend('extend')
print(f"""Cada letra como un elemento, modifica lista, no almacenable
lista.extend('extend') -> {lista}
-----""")
lista.extend(['extend'])
lista_extend = lista.extend(['extend_nueva'])
print(f"""Envuelto[], modifica lista, no almacenable
lista.extend(['extend']) -> {lista}
lista_extend_nueva = lista.extend(['extend_nueva']) -> {lista_extend}
-----""")
lista = ['cero', 'uno', 'dos', 'tres']
lista_nueva = lista + ['cuatro']
print(f"""Crear una nueva lista, no modifica, almacena
lista_nueva = lista + ['cuatro'] -> {lista_nueva}
-----""")




