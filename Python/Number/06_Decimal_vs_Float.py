from decimal import Decimal
libreria = '''
libreria -> from decimal import Decimal'''
print(libreria)
operación_float = '''
coste = 88.40
comisión = 0.08
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad)'''
print(operación_float)
coste = 88.40
comisión = 0.08
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad)

operación_decimal = '''
coste = Decimal(88.40)
comisión = Decimal(0.08)
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad)'''
print(operación_decimal)
coste = Decimal(88.40)
comisión = Decimal(0.08)
cantidad = 450

coste += (comisión * coste)
print(coste * cantidad)