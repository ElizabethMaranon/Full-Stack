"""
Función(argumentos)
  puede llevar condicional
"""
print('''-----
Función con argumentos''')
def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')

nombre_completo('Eli', 'Marañón')
print('''-----
Función con argumentos y condicionales''')
def autentificación(email, contraseña):
  if email == 'mielma@gmail.com' and contraseña == 'secreto':
    print('Autorizado')
  else:
    print('No autorizado')
autentificación('mielma@gmail.com', 'secreto')
print(f"""-----
Función sin argumentos""")
def centena():
  for num in range(1, 101):
    print(num)
centena()
print(f"""-----
Función dinámica, bucle """)
def contador(max):
  for num in range(1, max): # damos valor al maximo, siendo el tope sin imprimir este último
    print(num)
contador(7)


print("""-----
Coding Exercise""")
"""Create a function called greeting that prints "hello" when the function is called."""
def greeting():
  print('hello')
greeting()