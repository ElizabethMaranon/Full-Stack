print()
def saludo(momento_dia, *args, **kwargs):
  print(f"Hola {' '.join(args)}, espero que este teniendo una buena {momento_dia}")

  if kwargs:
    print('La tarea de hoy es:')
    for key, val in kwargs.items():
      print(f"{key} => {val}")

saludo('mañana', # argumento posicional
       'Eli', 'Marañón', # args -> Tupla
       primero = 'Poner Lavadora', #kwargs -> diccionario
       segundo = 'Colgar Lavadora',
       tercero = 'Recoger Lavadora')