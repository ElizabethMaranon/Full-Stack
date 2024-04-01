from decimal import Decimal
coste = 88.40
comisión = 0.08
cantidad = 450
coste += (comisión * coste)
print(f"""
libreria -> from decimal import Decimal
decimal es mucho mas preciso que float
-----
coste = 88.40
comisión = 0.08
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad) -> {coste * cantidad}
-----""")
coste = Decimal(88.40)
comisión = Decimal(0.08)
cantidad = 450
coste += (comisión * coste)
print(f"""coste = Decimal(88.40)
comisión = Decimal(0.08)
cantidad = 450
coste += (comisión * coste)
print(coste * cantidad) -> {coste * cantidad}

""")

