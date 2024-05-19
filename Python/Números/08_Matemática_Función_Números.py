import math
negativo = -20.25
positivo = 89.99


print(f"""
biblioteca -> import math
negativo = -20.25
positivo = 89.99
-----
abs -> valor absoluto elimina el negativo
abs(negativo) -> {abs(negativo)}
-----
math.floor -> redondea hacia abajo
(math.floor(positivo)) -> {(math.floor(positivo))}
(math.floor(negativo)) -> {(math.floor(negativo))}
-----
math.ceil -> redondea hacia arriba
(math.ceil(positivo))
(math.ceil(negativo))
(math.ceil(positivo))
(math.ceil(negativo))
-----
combina diferentes operaciones
(abs(math.ceil(positivo)))
(abs(math.ceil(negativo)))
(abs(math.floor(positivo)))
(abs(math.floor(negativo)))
-----
round -> redondea al numero más cercano
(round(positivo)) -> {(round(positivo))}
(round(negativo)) -> {(round(negativo))}
-----
math.sqrt -> raiz cuaddrada
negativo no tiene raiz cuadrada
(math.sqrt(positivo)) -> {(math.sqrt(positivo))}
-----
math.pow -> exponencial
(math.pow(5, 2)) resultado float -> {(math.pow(5, 2))} 
(math.pow(-5, 2))resultado float -> {(math.pow(-5, 2))}
-----""")