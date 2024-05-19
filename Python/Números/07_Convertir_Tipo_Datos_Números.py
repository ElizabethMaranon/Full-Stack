from decimal import Decimal
entero = 10
flot = 2.99
flot_entero = int(flot)
entero_flot = float(entero)
flot_dec = Decimal(flot)
flot_complejo = complex(flot)
print(f"""
biblioteca -> from decimal import Decimal
entero = 10
flot = 2.99
-----
Float -> Entero (eliminando float)
flot_entero = int(flot) -> {flot_entero}
print(int(flot) -> {int(flot)}
-----
Entero -> Float (poniendo float, entero.0)
entero_flot = float(entero)
print(flot_entero) -> {flot_entero}
print(float(entero)) -> {float(entero)}
-----
Float -> Decimal (poniendo decimales)
flot_dec = Decimal(flot)
print(flot_dec) -> {flot_dec}
print(Decimal(flot) -> {Decimal(flot)}
-----
Float -> Cientifico (notación cientifica)
flot_complejo = complex(flot)
print(flot_complejo = complex(flot)) -> {flot_complejo}
print(complex(flot) -> {complex(flot)}
-----""")
