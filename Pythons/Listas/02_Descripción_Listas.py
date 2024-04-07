usuarios = ['uno', 'dos', 'tres']
print(f"""
lista inicial
usuarios = ['uno', 'dos', 'tres']
print(usuarios) -> {usuarios}
-----""")
usuarios.insert(0, 'cuatro')
print(f"""insert -> añadir valores,index 0 primero, sino asignar uno
usuarios.insert(0, 'cuatro') 
print(usuarios) -> {usuarios}
-----""")
usuarios.append('cinco')
print(f"""append -> añadir valores sin indice, al final
usuarios.append('cinco') -> {usuarios}
-----
buscar un elemento en la lista index deseado
print(usuarios[0]) -> {usuarios[1]} imprime string
print([usuarios[1]]) ->{[usuarios[1]]} imprime lista
-----""")
usuarios[0] = 'seis'
print(f"""Reasignamos elemento de la lista
usuarios[index] = 'variable nueva'
usuarios[0] = 'seis' -> {usuarios}
""")
