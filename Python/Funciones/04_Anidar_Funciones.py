

print(f"""
Función dentro de otra función

def saludo(nombre, apellido):
  def nombre_completo():
    return f'{{nombre}} {{apellido}}'
  print(f'Hola {{nombre_completo()}}') 

saludo('Eli', 'Marañón')
      
resultado ->
      """)
def saludo(nombre, apellido):
  def nombre_completo():
    return f'{nombre} {apellido}'
  print(f'Hola {nombre_completo()}') 

saludo('Eli', 'Marañón')

print("""Coding Exercise
Create a function called greeting that accepts a persons name as an argument.
  Your function should return "Hello, {persons name}".

Example: Passing in 'Jordan' should return 'Hello, Jordan'""")

def greeting(nombre):
  return f'Hello, {nombre}'
print(greeting('Eli'))