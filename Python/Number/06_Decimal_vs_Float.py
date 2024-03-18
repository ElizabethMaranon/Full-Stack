from decimal import Decimal
libreria_decimal = '''from decimal import Decimal
libreria decimal función decimal 
para importar librería'''
decimal = '''
Aunque decimal está dentro de Python,
tendremos que llamarlo explícitamente
porque no podemos usarlo simplemente
de la misma manera que hemos usado otras funciones'''
print(decimal)
print(libreria_decimal)
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