Diccionario = {
    'lista': ['cero', 'uno', 'dos', 'tres'],
    'diccionario': {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3},
    'numero': (0, 1, 2, 3),
    'string': ('cero', 'uno', 'dos', 'tres'),
    'añadir elemento': ['nueva', 'lista']
}
busqueda = Diccionario['añadir elemento']
#Busqueda = Diccionario['buscar']
Buscar = Diccionario.get('buscar', 'Introducir el texto deseado en caso de no estar la clave') 
print(f'''
Buscamos la clave y nos devuelve el valor
busqueda = Diccionario['añadir elemento'] -> {busqueda}
-----
Si la clave no existe nos da keyError, distingue mayusculas,
para evitarlos usar get function, y nos devuelve el texto deseado en caso de error
Busqueda = Diccionario['Añadir elemento'] -> 
Buscar = Diccionario.get('buscar', 'Introducir el texto deseado en caso de no estar la clave') -> {Buscar}




''')