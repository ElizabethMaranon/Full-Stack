
print(f'''
Diccionario es un almacén de datos clave-valor,
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
en caso de no estar la clave
ortografia = diccionario['ortografia'] -> indica Key error''')
ortografia = diccionario['ortografia']
print(ortografia)