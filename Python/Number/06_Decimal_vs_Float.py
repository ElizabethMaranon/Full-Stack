from decimal import Decimal
print('''
libreria -> from decimal import Decimal''')
print('''
coste = 88.40
comisión = 0.08
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad)''')
coste = 88.40
comisión = 0.08
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad)

print('''
coste = Decimal(88.40)
comisión = Decimal(0.08)
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad)''')
coste = Decimal(88.40)
comisión = Decimal(0.08)
cantidad = 450

coste += (comisión * coste)
print(coste * cantidad)