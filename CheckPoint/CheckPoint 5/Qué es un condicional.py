"""Usuario y password para entrar en una página.
if -> Si ambos son correctos (afirmativo) se le permite la entrada,
elif -> Si ninguno de ellos es correcto (afirmativo), denegar acceso y ofrecer registrarse
else -> En caso contrario (negativo),  Alguno de los datos no es el correcto
"""
nombre = 'Mielma'
contraseña = 'secreto'

if nombre == 'Mielma' and contraseña == 'Secreto':
  print('Acceso permitido')
elif nombre != 'Mielma' and contraseña != 'Secreto':
  print('Sólo para usuarios registrados, ¿Desearías registrarte?')
else:
  print('Alguno de los datos no es el correcto')

