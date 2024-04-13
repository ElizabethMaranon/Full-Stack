from functools import reduce
print('''
libreria -> from functools import reduce ''')
print('-----')
print('''exponente manual iterante
def exp_man_ite(numero, exponente):
  contador = exponente -1
  total = numero

  while contador > 0:
    total *= numero
    contador  -= 1
  return total

print(exp_man_ite(2, 3))
print(exp_man_ite(3, 2))''')

def exp_man_ite(numero, exponente):
  contador = exponente -1
  total = numero

  while contador > 0:
    total *= numero
    contador  -= 1
  return total

print(exp_man_ite(2, 3))
print(exp_man_ite(3, 2))
print('''-----''')
print('''exponente manual funcional
[numero3] * exponente2 (lista) -> [3, 3]
def exp_man_fun(numero, exponente):
  lista_computada = [numero] * exponente
  return (reduce(lambda total, element: total * element, lista_computada)) ''')
def exp_man_fun(numero, exponente):
  lista_computada = [numero] * exponente
  return (reduce(lambda total, element: total * element, lista_computada))
print(exp_man_fun(2, 3))
print(exp_man_fun(3, 2))