nombre = 'Mielma'
email = 'Mielma@gmail.com'
contraseña = 'password'
print(f"""
nombre = 'Mielma'
email = 'Mielma@gmail.com'
contraseña = 'password'
-----
Buscar varias condiciones con operador if
and(todas)
or(minimo una de ellas)
and not(valor falso)
      
if nombre == 'Mielma' and contraseña == 'password':
  print('Acceso permitido')
else:
  print('Acceso no autorizado')

resultado ->""")
if nombre == 'Mielma' and contraseña == 'password':
  print('Acceso permitido')
else:
  print('Acceso no autorizado')
print(f"""-----
Anidar las condiciones if if if, no recomendada
      
if nombre == 'Mielma':
  if contraseña == 'password':
    print('Acceso permitido')
else:
  print('Acceso no autorizado')

resultado ->""")
if nombre == 'Mielma':
  if contraseña == 'password':
    print('Acceso permitido')
else:
  print('Acceso no autorizado')

print(f"""-----
Podemos poner más de dos condiciones

if (nombre =='Mielma' or email == 'Mielma@gmail.com') and contraseña == 'password':
  print('Acceso permitido')
else:
  print('Acceso no autorizado')

resultado ->""")

if (nombre =='Mielma' or email == 'Mielma@gmail.com') and contraseña == 'password':
  print('Acceso permitido')
else:
  print('Acceso no autorizado')

print(f"""
Condiconal no verdadera

logeado = True
vip = True
if logeado and not vip: # logeado verdadero, vip falso
  print('Usuario Estandar') 
else:
  print('Usuario vip')
resultado ->""")
logeado = True
vip = True
if logeado and not vip:
  print('Usuario Estandar')
else:
  print('Usuario vip')

print(f"""
Coding Exercise
Fill in the below conditional with a compound condition that will print "Success!"
if "number" is anything between 1 and 100 (inclusive).
if #YourCompoundConditionalHere:
   print("Success!")
else:
   print("Failure...")
-----
number = 7
if number >= 1 and number <= 100:
  print("Success!")
else:
  print("Failure...")

resultado ->""")
number = 7
if number >= 1 and number <= 100:
  print("Success!")
else:
  print("Failure...")