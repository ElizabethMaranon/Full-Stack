Diccionario ={
    'lista': ['cero', 'uno', 'dos', 'tres'],
    'diccionario': {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3},
    'numero': (0, 1, 2, 3),
    'string': ('cero', 'uno', 'dos', 'tres')
}
lista = Diccionario['lista']
diccionario = Diccionario['diccionario']
numero = Diccionario['numero']
string = Diccionario['string']

print(f"""
Las claves pueden tener valor numerico, string, diccionario, lista, tupla....
Diccionario ={{
    'lista': ['cero', 'uno', 'dos', 'tres'],
    'diccionario': {{'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3}}
    'numero': (0, 1, 2, 3),
    'string': ('cero', 'uno', 'dos', 'tres')}}
-----
podemos imprimir el diccionario entero {{Diccionario}}
{Diccionario}

imprimir la clave  {{Diccionario['key_asignada']}}
{Diccionario['lista']}
{Diccionario['diccionario']}
{Diccionario['numero']}
{Diccionario['string']}
-----
Las listas que estan dentro de una biblioteca podemos usarlas como una lista normal,
haciendo busqueda, slice,.... por ejemplo
{{Diccionario['lista'][:2]}} -> {Diccionario['lista'][:2]}
-----
Podemos guardar los valores de una clave como una variable
lista = Diccionario['lista'] -> {lista}
diccionario = Diccionario['diccionario'] -> {diccionario}
numero = Diccionario['numero'] -> {numero}
string = Diccionario['string]'] -> {string}

""")