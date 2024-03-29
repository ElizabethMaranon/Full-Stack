print('''
rangos = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
-----''')
lista = [
  'cero',
  'uno',
  'dos',
  'tres',
  'cuatro',
  'cinco',
  'seis'  
]
print('segundo_penultimo = lista[1:-1]')
segundo_penultimo = lista[1:-1]
print(segundo_penultimo)
print('''-----''')
primer_penultimo_intervalo = lista[:-1:2]
print(primer_penultimo_intervalo)
print('''-----''')
print('''invertir_index = lista[::-1]''')
invertir_index = lista[::-1]
print(invertir_index)