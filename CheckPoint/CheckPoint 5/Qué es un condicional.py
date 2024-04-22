nombre = 'Mielma'
contraseña = 'secreto'

if nombre == 'Mielma' and contraseña == 'Secreto':
  print('Acceso permitido')
elif nombre != 'Mielma' and contraseña != 'Secreto':
  print('Sólo para usuarios registrados, ¿Desearías registrarte?')
else:
  print('Alguno de los datos no es el correcto')

