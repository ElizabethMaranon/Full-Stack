from decimal import Decimal
print('''
from decimal import Decimal''')
entero = 10
flot = 2.99
print('''entero = 10
flot = 2.99
''')
print(
'''
Float -> Entero (eliminando float)''')
flot_entero = int(flot)
print('''flot_entero = int(flot)
print(flot_entero)''')
print(flot_entero)
print('''print(int(flot))''')
print(int(flot))
print('''
-----''')
print('''
Entero -> Float (poniendo float, entero.0)''')
entero_flot = float(entero)
print('''entero_flot = float(entero)
print(flot_entero)''')
print(flot_entero)
print('''print(float(entero))''')
print(float(entero))
print('''
-----''')
print('''
Float -> Decimal (poniendo decimales)''')
flot_dec = Decimal(flot)
print('flot_dec = Decimal(flot)')
print('print(flot_dec)')
print(flot_dec)
print('print(Decimal(flot))')
print(Decimal(flot))
print('''
-----''')
print('''
Float -> Cientifico (notación cientifica)''')
flot_complejo = complex(flot)
print('flot_complejo = complex(flot)')
print('print(flot_complejo = complex(flot))')
print(flot_complejo)
print('print(complex(flot))')
print(complex(flot))
print('''
-----''')
