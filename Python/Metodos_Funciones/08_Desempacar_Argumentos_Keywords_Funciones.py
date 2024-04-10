def keywords (**kwargs):
  print(kwargs)
print(f"""
Doble asterisco y kwargs (no obligatoria pero si habitual)
def keywords (**kwargs):
  print(kwargs)
->""")
keywords()
print(f"""Devuelve {{}}, diccionario, tiene key y value
      
keywords(clave = 'Valor', clave2 = 'Valor2')
->""")
keywords(clave = 'Valor', clave2 = 'Valor2')

def condicional(**kwargs):
  if kwargs:
    print(f"Condicional con if, {kwargs['Key']} {kwargs['Key2']}, estás en el diccionario")
  else:
    print(f"No estas registrado")
print(f"""
def condicional(**kwargs):
  if kwargs:
    print(f"Condicional con if, {{kwargs['Key']}} {{kwargs['Key2']}}, estás en el diccionario")
  else:
    print(f"No estas registrado")
      
condicional(Key = 'valor', Key2 = 'valor2')
condicional()
->""")
condicional(Key = 'valor', Key2 = 'valor2')
condicional()