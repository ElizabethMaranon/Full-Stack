nombre = 'Eli'
apellido = 'Marañón'
def nombre_completo(nombre, apellido):
  print(f'{nombre} {apellido}')


print(f"""
Diferenciar entre imprimir y devolver valor
      
Imprimir -> print()
  * Imprime Items en la consola
  * No se hace en la vida real
    * Excepto en depuración y quieres ver cual es la salida de la fucnión
Resultado -> {nombre_completo('Eli', 'Marañón')}""")

print(f"""-----
Retornar valor -> return()
  * Se hace en los programas
  * Retorna la acción de la función, la ejecuta
Resultado-> #  no se imprime pero si se ejecuta""")
nombrer = 'Eli'
apellidor = 'Marañón'
def nombre_completor(nombrer, apellidor):
  return f'{nombrer} {apellidor}'
nombre_completor('Eli', 'Marañón')
print(f"""
Se Puede guardar en una variable para poder imprimirla después
eli = nombre_completor('Eli', 'Marañón')
def saludo(name):
  print(f'¡hola {{name}}!')""")
eli = nombre_completor('Eli', 'Marañón')
def saludo(name):
  print(f'¡hola {name}!')
saludo(eli)



print(f"""Coding Exercise
Create a function called sum_two_numbers that accepts two arguments. The function should 'return' the total of those two arguments added together.""")
def sum_two_numbers(num1, num2):
  return(num1 + num2)
print(sum_two_numbers(1, 2))
