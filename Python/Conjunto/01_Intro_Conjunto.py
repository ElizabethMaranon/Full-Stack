print(f"""
Un conjunto es una especie de combinación de diccionario y lista.
Llaves como el diccionario, sin clave/valor,
Elementos como en lista, pero sin su funcionalidad
Requiere que todos los elementos sean únicos.
No pueda haber duplicados.
-----""")
conjunto = {'uno', 'dos', 'tres'}
print(f"""conjunto = {{'uno', 'dos', 'tres'}} -> {conjunto}""")
conjunto = {'uno', 'dos', 'tres', 'uno'}     
print(f"""
El elemento duplicado no se imprime
conjunto = {{'uno', 'dos', 'tres', 'uno'}} -> {conjunto}
-----
print(conjunto[0]) -> Error, porque no se puede usar index
-----""")
consulta_uno = 'uno' in conjunto
consulta_cuatro = 'cuatro' in conjunto
print(f"""hacer una consulta por elemento, devuelve boolean
consulta_uno = 'uno' in conjunto -> {consulta_uno}
consulta_cuatro = 'cuatro' in conjunto -> {consulta_cuatro}
""")


