from functools import reduce
print('''
libreria -> from functools import reduce ''')
print('''
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
print('''
-----
''')