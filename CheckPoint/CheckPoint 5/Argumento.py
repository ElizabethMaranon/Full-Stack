
def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')
#Argumento posicional
nombre_completo('Mielma', 'Developer')
#nombre argumento, no tiene que ir en orden, pero tiee
nombre_completo(nombre = 'Mielma', apellido = 'Developer')
nombre_completo(apellido = 'Developer', nombre = 'Mielma')