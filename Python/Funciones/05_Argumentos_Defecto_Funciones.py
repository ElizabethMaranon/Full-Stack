print(f"""
Argumento por defecto, en caso de no tener argumento

def saludo(argumento = 'Por defecto'):
  print(f'Hola, {{argumento}}')

saludo() # Sin argumento, imprime por defecto
saludo('Eli') # Con argumento, omite por defecto
""")
def saludo(argumento = 'Por defecto'):
  print(f'Hola, {argumento}')

saludo() 
saludo('Eli')

"""
Mala práctica poner colección como argumento.
A volver a llamar la función, recuerda el valor anterior
      
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection

print(some_function())
print(some_function())
"""

print(f"""
Coding Exercise"""
"""Create a function called counter that accepts an argument called initial_count
and returns that argument incremented by 1. initial_count must have a default value of 0.
""")

def counter(initial_count = 0):
  return initial_count +1

print(counter())



