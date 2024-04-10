def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')

nombre_completo('Nombre', 'Apellido')
nombre_completo('Eli', 'Marañón')

print(f"""
Los argumentos posicionales van en el mismo orden que los hemos puesto.
Si hay muchos argumentos, puede crear error, por omisión o confusión en el orden
def nombre_completo(nombre, apellido):
  print(f'{{nombre}} {{apellido}}')

nombre_completo('Nombre', 'Apellido')
nombre_completo('Eli', 'Marañón')""")
def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')
print('->')
nombre_completo('Nombre', 'Apellido')
nombre_completo('Eli', 'Marañón')

print(f"""
Cuando hay muchos argumentos, llamarlos con el nombre del argumento,
como si estuvieramos creando una variable,
no es necesario argumentar en el mismo orden
si faltara algun argumetno, error...

nombre_completo(nombre = 'Eli', apellido = 'Marañón')
nombre_completo(apellido = 'Marañón', nombre = 'Eli')

->""")
nombre_completo(nombre = 'Eli', apellido = 'Marañón')
nombre_completo(apellido = 'Marañón', nombre = 'Eli')

print(f"""
Coding Exercise
Behind the scenes of the code test is a function called sequence
that accepts 5 arguments: first, second, third, fourth, and fifth.
Unfortunately, they are not in sequential order.
Using named arguments, call the sequence function and pass in the 5 arguments,
setting their values to 1, 2, 3, 4, 5 respectively.
      
def named_arguments_practice(sequence):
    sequence(first = 1, second = 2, third = 3, fourth = 4, fifth = 5)
    return sequence
-> """)

def named_arguments_practice(sequence):
    sequence(first = 1, second = 2, third = 3, fourth = 4, fifth = 5)
    return sequence

