print(f"""
Lista por comprensión es un conjunto de bucles for-in y condicionales que pueden colocarse dentro de una sola línea de código
Puedes escribir este código con varias líneas y luego puedes hacer referencias cruzadas""")
nombre_lista = range(1, 11)
variable_de_iteracion = []
for variable_new in nombre_lista:
  variable_de_iteracion.append(variable_new ** 3)

nums_variable_de_iteracion = [variable_new ** 3 for variable_new in nombre_lista] 

pares = []
for variable_new in nombre_lista:
  if variable_new % 2 == 0:
    pares.append(variable_new)

pares_comprensivo = [variable_new for variable_new in nombre_lista if variable_new % 2 == 0]

print(f"""
Forma tradicional

nombre_lista = range(1, 11)
variable_de_iteracion = []
for variable_new in nombre_lista:
  variable_de_iteracion.append(variable_new ** 3)

Resultado -> {variable_de_iteracion}
-----
Lista Comprensiva
variable = [acción for variable_new in nombre_lista:]
nums_variable_de_iteracion = [variable_new ** 3 for variable_new in nombre_lista] # Generar dinamicamente una lista
resultado -> {nums_variable_de_iteracion}
-----
Añadir condicional tradicional

pares = []
for variable_new in nombre_lista:
  if variable_new % 2 == 0: # % modulo, saber si tiene resto(impar) o no(par),
    pares.append(variable_new)
resultado-> {pares}
-----
Añadir condicional Lista comprensiva

pares_comprensivo = [variable_new for variable_new in nombre_lista if variable_new % 2 == 0]
resultado -> {pares_comprensivo}

  """)
numbers = [1,2,3,4,5,6]
result = [num +1  for num in numbers]

print(f'''
Coding Exercise
Create a variable called result and use list comprehension
to increment each number from the numbers list by 1.

def list_comprehension():
    numbers = [1,2,3,4,5,6]
    result = [num +1  for num in numbers]
    
    return result
      {result}''')

