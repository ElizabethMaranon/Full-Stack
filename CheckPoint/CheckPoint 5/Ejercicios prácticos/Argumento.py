# Mismo resultado con diferente manera de argumentos

def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')
print("""
Argumento posicional
      """)
nombre_completo('Mielma', 'Developer')
print("""-----
Nombre argumento, no tiene que ir en orden
      """)
nombre_completo(nombre = 'Mielma', apellido = 'Developer')
nombre_completo(apellido = 'Developer', nombre = 'Mielma')
print("""-----
Argumento por defecto
      """)
def saludo(argumento = 'Invitado'):
  print(f'Hola, {argumento}')
saludo() # Sin argumento, imprime por defecto
saludo('Eli') # Con argumento, omite por defecto