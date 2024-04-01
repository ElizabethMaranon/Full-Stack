usuarios = ['Eli', 'Ivan', 'Hades', 'Gara', 'Elli']
print("""
lista inicial
usuarios = ['Eli', 'Ivan', 'Hades', 'Gara', 'Elli']
print(usuarios) -> {usuarios}
-----""")
print("""
Remove -> extrae elemento elegido
usuarios.remove('Eli') -> {usuarios}
-----""")
usuario_pop = usuarios.pop()
print("""
Pop -> expulsa último elemento
pop no elimina, rescata para que puedas usar
se guardan en la variable_pop creada
usuario_pop = usuarios.pop()
print(usuarios) -> {usuarios}
print(usuario_pop) -> {usuario_pop}
-----""")
del usuarios[0]
print("""del -> eliminar
del usuarios[index]
del usuarios[0]
print(usuarios) -> {usuarios}
-----""")




