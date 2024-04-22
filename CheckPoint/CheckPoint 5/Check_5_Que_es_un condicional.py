"""¿Qué es un condicional?
Los condicionales sirven para automatizar el programa, es decir, acatan las órdenes y se ejecutan dependiendo de la orden recibida, el programa funcionará de una manera u otra dependiendo de la condición.
If -> Condiciones que deben cumplirse
and(todas)
or(minimo una de ellas)
and not(valor falso)
Elif-> Otras condiciones que tendrían que cumplirse
Else -> En caso de no cumplirse las condiciones anteriores
Ejemplo: 
Usuario y password para entrar en una página.
Si ambos son correctos (afirmativo) se le permite la entrada, diferencia las mayúsculas de las minúsculas.
En caso contrario (negativo),se le prohíbe la entrada
"""

nombre = 'Mielma'
contraseña = 'Password'

if nombre == 'Mielma' and contraseña == 'password':
  print('Acceso permitido')
elif nombre != 'Mielma' and contraseña != 'password':
  print('Sólo para usuarios registrados, ¿Desearías registrarte?')
else:
  print('Alguno de los datos no es el correcto')

