Tupla = ('Bat', 'Bi', 'Hiru', 'Lau', 'Bost')
Tupla = Tupla[:-1]
Tupla = Tupla[1:]

print(f"""
Tupla inmutable, por lo que realmente no se eliminaran de la tupla original
Crear nuevas tuplas eliminando elementos
Tres maneras, la tercera truco, mala practica.

Tupla original
Tupla = ('Bat', 'Bi', 'Hiru', 'Lau', 'Bost')
      
1º Eliminar elementos desde el final con index deseado
Tupla = Tupla[:-1] -> {Tupla}

2º Eliminar elementos desde el principio con index deseado
Tupla = Tupla[:-1] -> {Tupla}""")
Lista = list(Tupla)
Lista.remove('Hiru')
Tupla = tuple(Lista)
print(f"""
3º Eliminar elemento especificado(mala práctica, no recomndado)
convertimos en lista, peligro
Lista = list(Tupla)
Lista.remove('Hiru') -> {Lista}
Tupla = tuple(Lista) -> {Tupla}
""")


