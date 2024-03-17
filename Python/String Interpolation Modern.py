'''
Objetivo
brindar capacidad de ejecuta codigo Python dentro de una cadena de texto
'''
nombre = 'Eli'
letra_f = 'letra efe colocada antes de las comillas para indicar que es una cadena de texto'
print(letra_f)
funcion = f'hola {nombre} la variable entre corchetes,  incluso operaciones matematicas,'
print(funcion)
corchete = f'hola {nombre}, {{escribe doble corchete para imprimir corchete}}'
print(corchete)
producto = 'Curso Python'
mielma = 'Mielma Developer'
email_contenido = f'''
Hola {nombre}:

Su aprendizaje {producto} se esta cursando.

Espero lo disfrute.

Atentamente, {mielma}
'''
#print(email_contenido)

'''Coding Exercise'''
first_name = 'Elizabeth'
last_name = 'Marañón'
greeting = f'Hello, {first_name} {last_name}'
#print(greeting)

'''Use Python's format method to Implement Index Based String Interpolation'''
edad = 44
saludo = 'Hola {0}, apareces en la lista con edad de {1} y estas cursando: {2}. Atentamente {3}'.format(nombre, edad, producto, 'Mielma')#format(0, 1, 2, 3...)cada numero indica el numero de variable
print(saludo)
