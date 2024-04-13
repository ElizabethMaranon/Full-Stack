"""
Construir u programa que imprima números del 1 al 100, definiendo valor máximo.
Multiplos de 3 imprimir Fizz.
Multiplos de 5 imprimir Buzz.
Multiplos de 3  y 5 imprimir FizzBuzz.     
      
Usar Funciones - Bucle - Condicionales - Operaciones matemáticas"""

def FizzBuzz (max_numero): 
  for numero in range(1, max_numero + 1): 
    if numero % 3 == 0 and numero % 5 == 0: 
      print('FizzBuzz')
    elif numero % 5 == 0: 
      print('Buzz')
    elif numero % 3 == 0:
      print('Fizz')
    else:
      print(numero)

FizzBuzz(100)

"""Explicación del proceso
      
# Función FizzBuzz con valor maximo      
def FizzBuzz (max_numero):
  # Si el número está en el rango (bucle) de 1 y max+1(+1 porque imprime hasta el número anterior)
  for numero in range(1, max_numero + 1):
    # Si al dividir entre 3 y 5 no hay resto
    if numero % 3 == 0 and numero % 5 == 0:
      # Valor a devolver
      print('FizzBuzz')
    # Si condicional anterior falsa -> si al dividir entre 5 no hay resto
    elif numero % 5 == 0:
      # Valor a devolver
      print('Buzz')
    # Si condicional anterior falsa -> si al dividir entre 3 no hay resto 
    elif numero % 3 == 0:
      # Valor a devolver 
      print('Fizz')
    # En caso de que las condicionales aneriores sean falsas todas
    else:
      # Valor a devolver
      print(numero) """
