lista = [
  'cero',
  'uno',
  'dos',
  'tres',
  'cuatro',
  'cinco',
  'seis'  
]
segundo_penultimo = lista[1:-1]
primer_penultimo_intervalo = lista[:-1:2]
invertir_index = lista[::-1]
print(f"""
rangos = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
-----
segundo_penultimo = lista[1:-1] -> {segundo_penultimo}
-----
primer_penultimo_intervalo = lista[:-1:2] -> {primer_penultimo_intervalo}
-----
invertir_index = lista[::-1] -> {invertir_index}
""")
