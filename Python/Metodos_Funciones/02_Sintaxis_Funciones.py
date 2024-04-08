print(f"""
Función(argumentos)
  puede llevar condicional

Función con argumentos          
def nombre_completo(nombre, apellido):
  print('Hola')
  #dos lineas espacio

nombre_completo('Eli', 'Marañón')
->""")
def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')


nombre_completo('Eli', 'Marañón')

print(f"""-----
Función con argumentos y condicionales      
def autentificación(email, contraseña):
  if email == 'mielma@gmail.com' and contraseña == 'secreto':
    print('Autorizado')
  else:
    print('No autorizado')
autentificación('mielma@gmail.com', 'secreto')
-> """)

def autentificación(email, contraseña):
  if email == 'mielma@gmail.com' and contraseña == 'secreto':
    print('Autorizado')
  else:
    print('No autorizado')
autentificación('mielma@gmail.com', 'secreto')
print(f"""-----
Función sin argumentos

def centena():
  for num in range(1, 101):
    print(num)
centena()
-> """)
def centena():
  for num in range(1, 101):
    print(num)
centena()
print(f"""-----
Función dinámica, bucle

def contador(max):
  for num in range(1, max):
    print(num)
contador(7) # damos valor al maximo, siendo el tope sin imprimir este último
-> """)
def contador(max):
  for num in range(1, max):
    print(num)
contador(7)

print(f"""
Coding Exercise
Create a function called greeting that prints "hello" when the function is called.
      
def greeting():
  print('hello')
greeting()

resultado -> """)
def greeting():
  print('hello')
greeting()