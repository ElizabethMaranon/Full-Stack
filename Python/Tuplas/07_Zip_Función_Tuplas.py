idioma = ['Euskera', 'Castellano', 'Inglés']
saludo = ['Kaixo', 'Hola', 'Hello']
Fusionar = zip(idioma, saludo)


print(f"""
Zip -> Fusionar listas en un conjunto de tuplas
Muy importante que esten los elementos bien ordenados
Fusionar = zip(idioma, saludo) -> {Fusionar}
convertirlo en lista
print(list(Fusionar)) -> {list(Fusionar)}
""")