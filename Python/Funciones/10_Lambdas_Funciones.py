"""
Lambda es una herramienta que nos permite empaquetar una función,
normalmente mas pequeña e introducirla en otras funciones.
Son moviles y faciles de usar
Toma una variable (varios nombres) devuelve una cadena formateada
-----"""
sobrenombre = lambda nombre, apellido: f'{nombre} {apellido}'
print(f"""{sobrenombre('Mielma', 'Developer')}
-----""")
def saludo(apodo):
  print(f'Hola {apodo}')

saludo(sobrenombre('Mielma', 'Developer'))

print(f"""-----""")
"""Coding Exercise
In the code below, create a variable called "greeting" and assign it a lambda function that accepts a name as an argument, and return the string "Hi, name".

Example: If you pass in the name "Jordan", it should return "Hi, Jordan"."""

def lambda_practice():
    greeting = lambda name : f'Hi {name}'
    
    return greeting
