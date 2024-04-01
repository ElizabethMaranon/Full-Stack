
print(f'''
Diccionario es un almacén de datos pares clave-valor,
''')
diccionario = {
    'key': 'value',
    'clave': 'valor',
    'color': 'morado',
    'numero': 7,
    'musica': 'folk-metal'
}
print(f'''Creamos nuestro diccionario
diccionario = {{
    'key': 'value',
    'clave': 'valor',
    'color': 'morado',
    'numero': 7,
    'musica': 'folk-metal'
}}
y así es como se queda guardada
{diccionario}''')
print('''-----''')
color_fav = diccionario['color']
print(f'''No tiene index, sino key
para saber el valor buscamos la clave,
color_fav = diccionario['color] - > {color_fav}
Si la clave no está nos da error, distingue las mayusculas
Color = diccionario['Color'] ->''')
Color = diccionario['Color']
print(Color)