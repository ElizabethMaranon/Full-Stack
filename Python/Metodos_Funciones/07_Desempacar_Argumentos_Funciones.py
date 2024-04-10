def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')

nombre_completo('Eli', 'Marañón')
print(f"""
Simbolo * al principio para desempacar luego llamar a argumentos(args, aconsejado pero no es clave obligatoria)
def desempacar(*args):
  print(f'Desempacar, ' + ' '.join(args),'dejar en blanco con comillas donde irán los argumentos') 
desempacar('argumentos', 'tantos', 'como', 'necesites') -> 
->""")
def desempacar(*args):
  print(f'Hola, ' + ' '.join(args),'dejar en blanco con comillas donde irán los argumentos o añadir lo que necesitos al argumento') 
desempacar('argumentos', 'tantos', 'como', 'necesites')
print(f"""-----
def tupla(*args):
  print(args)
  print('Nos devuelve los argumentos en forma de tupla')
tupla('1', '2')
->""")
def tupla(*args):
  print(args)
  print('Nos devuelve los argumentos en forma de tupla')
tupla('1', '2')
print(f"""-----
def varios_argumentos(posicional_tradicional, *args):
  print(f"primero irá {{posicional_tradicional}} y luego {{' '.join(args)}}")
varios_argumentos('tracional', 'arg1', 'arg2', 'tantos como queramos')
""")
def varios_argumentos(posicional_tradicional, *args):
  print(f"primero irá {posicional_tradicional} y luego {' '.join(args)}")
varios_argumentos('tracional', 'arg1', 'arg2', 'tantos como queramos')