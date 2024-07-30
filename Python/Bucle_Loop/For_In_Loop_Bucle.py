listas = ['uno', 'dos', 'tres', 'cuatro']
tuplas = ('uno', 'dos', 'tres', 'cuatro')
diccionarios = {'uno':'bat', 'dos':'bi', 'tres':'hiru', 'cuatro':'lau'}
"""for-in-loop
Tiene principio y fin. Bucle acaba cuando acaban los elementos
Python despues de : mayoritariamente sangría
Consejo: si la colección está en plural, usar la variable bloque en singular,
aunque podemos usar el nombre que queramos

Listas y Tuplas
for variable in variables:
  print(variable) Sangría obligatoria, sino error

Diccionario tenemos que darle dos nombres, key y valor
for key, valor in diccionarios.items():
  print('key', key)
  print('valor', valor)"""
print("""Diccionario
      """)
for español, euskera in diccionarios.items():
  print('español', español)
  print('euskera', euskera)
print("""
-----
Listas
      """)
for lista in listas:
  print(lista)
print("""-----
tupla
""")
for tupla in tuplas:
  print(tupla)
print("""-----
Coding Exercise
      """)

"""

Create a list named my_list with 5 elements.
Then loop over the list to print out each element.

def loop_over_list():
    my_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    for lista in my_list:
        print(lista)
    return my_list
"""
my_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
for lista in my_list:
    print(lista)

