diccionario = {
    'key': 'value',
    'clave': 'valor',
    'color': 'morado',
    'numero': 7,
    'musica': 'folk-metal'
}
grupo_diccionario = diccionario.items()
elementos_anidados = {
    'primero': ['diez', 'once'],
    'segundo': ['veinte', 'veintiuno'],
    'tercero': ['treinta', 'treintayuno'],
    'cuarto': ['cuarenta', 'cuarentayuno']
}
grupo_elementos_anidados = elementos_anidados.items()
print(f'''
diccionario = {{
    'key': 'value',
    'clave': 'valor',
    'color': 'morado',
    'numero': 7,
    'musica': 'folk-metal'
}}
      
grupo_diccionario = diccionario.items() {grupo_diccionario}
      
-----

Crear objeto vista, sólo para poder visualizar, no para trabajar con los datos obtenidos, exceptuando len, iter, in
Si hacemos una consulta y alguien ha cambiado el diccionario, el resultado de la consulta cambiará
Evitar imprimir cambios en el diccionario, haciendo una copia de los valores
diccionario_copia = print(list(diccionario.copy().values())) -> {list(diccionario.copy().values())}

-----

Imprimir clave
devuelva como lista, pero no es una lista verdadera o convertir en lista
print(diccionario.keys()) -> {diccionario.keys()}
print(list(diccionario.keys())) -> {list(diccionario.keys())}

-----

Imprimir valores
devuelva como lista, pero no es una lista verdadera o convertir en lista
print(diccionaio.values()) -> {diccionario.values()}
print(list(diccionario.values())) -> {list(diccionario.values())}

-----

Imprime elemento, tupla, lista, dentro de una lista
devuelva como tupla, pero no es una tupla verdadera o convertir en lista
print(diccionario.items()) ->{diccionario.items()}
print(list(diccionario.items())) -> {list(diccionario.items())}
print(list(grupo_diccionario)[1]) -> {list(grupo_diccionario)[1]}


-----

Podemos hacer lo mismo con los elementos anidados
elementos_anidados = {{
    'primero': ['diez', 'once'],
    'segundo': ['veinte', 'veintiuno'],
    'tercero': ['treinta', 'treintayuno'],
    'cuarto': ['cuarenta', 'cuarentayuno']
}}

grupo_elementos_anidados = elementos_anidados.items()

-----

print(elementos_anidados.items()) -> {elementos_anidados.items()}
print(list(elementos_anidados.items())) -> {list(elementos_anidados.items())}
print(list(grupo_elementos_anidados)[1]) -> {list(grupo_elementos_anidados)[1]}
print(list(grupo_elementos_anidados)[1][1]) -> {list(grupo_elementos_anidados)[1][1]}
print(list(grupo_elementos_anidados)[1][1][0]) -> {list(grupo_elementos_anidados)[1][1][0]}
print(list(grupo_elementos_anidados)[index_key][matriz][index])
-----
Resources
https://docs.python.org/3.0/library/stdtypes.html#dictionary-view-objects
''')