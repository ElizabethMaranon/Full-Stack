'''Use Python's format method to Implement Index Based String Interpolation'''
nombre = 'Eli'
producto = 'Curso Python'
mielma = 'Mielma Developer'
edad = 44
saludo = '''Hola {0}, apareces en la lista con edad de {1}
y estas cursando: {2}. Atentamente {3}'''.format(nombre, edad, producto, mielma)
#format(0, 1, 2, 3...)cada numero indica el numero de variable
print(f"""
nombre = 'Eli'
producto = 'Curso Python'
mielma = 'Mielma Developer'
edad = 44
saludo = '''Hola {{0}}, apareces en la lista con edad de {{1}}
y estas cursando: {{2}}. Atentamente {{3}}'''.format(nombre, edad, producto, 'Mielma')
#format(0, 1, 2, 3...)cada numero indica el numero de variable

{saludo}""")