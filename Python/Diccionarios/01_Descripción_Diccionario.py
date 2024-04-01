diccionario = {
    'key': 'value',
    'clave': 'valor',
    'color': 'morado',
    'numero': 7,
    'musica': 'folk-metal'
}
color_fav = diccionario['color']
color = diccionario['color']
print(f"""
Diccionario es un almacén de datos pares clave-valor,

diccionario = {{
    'key': 'value',
    'clave': 'valor',
    'color': 'morado',
    'numero': 7,
    'musica': 'folk-metal'
}}
y así es como se queda guardada
{diccionario}
-----
color_fav = diccionario['color']
No tiene index, sino key
para saber el valor buscamos la clave,
color_fav = diccionario['color] - > {color_fav}
Si la clave no está nos da error, distingue las mayusculas
color = diccionario['color'] -> {color}
Color = diccionario['Color'] -> NameError: name 'Color' is not defined

""")