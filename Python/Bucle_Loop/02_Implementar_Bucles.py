listas = ['uno', 'dos', 'tres', 'cuatro']
tuplas = ('uno', 'dos', 'tres', 'cuatro')
diccionarios = {'uno':'bat', 'dos':'bi', 'tres':'hiru', 'cuatro':'lau'}
print(f"""
listas = {listas}
tuplas = {tuplas}
-----
for-in-loop
Python despues de : mayoritariamente sangría
Consejo: si la colección está en plural, usar la variable bloque en singular,
aunque podemos usar el nombre que queramos

Listas y Tuplas
for variable in variable:
  print(variable) Sangría obligatoria, sino error

Diccionario tenemos que darle dos nombres, key y valor
for key, valor in diccionarios.items():
  print('key', key)
  print('valor', valor)
-----
for lista in listas:
  print(listas) -> """)
for lista in listas:
  print(lista)
print("""-----
for tupla in tuplas:
  print(tupla)""")
for tupla in tuplas:
  print(tupla)
print("""-----
for español, euskera in diccionarios.items():
  print('español', español)
  print('euskera', euskera)""")
for español, euskera in diccionarios.items():
  print('español', español)
  print('euskera', euskera)

print(f"""
Coding Exercise
Create a list named my_list with 5 elements.
Then loop over the list to print out each element.

def loop_over_list():
    my_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    for lista in my_list:
        print(lista)
    return my_list
""")
my_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
for lista in my_list:
    print(lista)

