conjunto1 = {'uno', 'dos', 'tres'}
conjunto2 = {'uno', 'dos', 'tres', 'uno'} 
consulta_uno = 'uno' in conjunto1
consulta_cuatro = 'cuatro' in conjunto1
print(f"""
Un conjunto es una especie de combinación de diccionario y lista.
Llaves como el diccionario, sin clave/valor,
Elementos como en lista, pero sin su funcionalidad
Requiere que todos los elementos sean únicos.
No pueda haber duplicados.
-----
conjunto1 = {{'uno', 'dos', 'tres'}} -> {conjunto1}
-----
El elemento duplicado no se imprime
conjunto2 = {{'uno', 'dos', 'tres', 'uno'}} -> {conjunto2}
-----
print(conjunto[0]) -> Error, porque no se puede usar index
-----
Hacer una consulta por elemento, devuelve boolean
consulta_uno = 'uno' in conjunto1 -> {consulta_uno}
consulta_cuatro = 'cuatro' in conjunto1 -> {consulta_cuatro}
""")


