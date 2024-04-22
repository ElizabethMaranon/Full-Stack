cadena = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
numeros = [1, 2, 3, 4, 5]
combinada = ['uno', 43, 1.5]
listas = [['uno', 'dos', 'tres', 'cuatro', 'cinco'], [1, 2, 3, 4, 5], 'listas anidadas']
listas_anidadas = [cadena, numeros, 'listas anidadas']
"""diferentes listas
listas combinadas son peligrosas por si hay funciones en bucle
listas anidadas, pueden contener otras listas como elemento"""
print(f"""-----
cadena -> {cadena}
-----
numeros -> {numeros}
-----
combinada -> {combinada}
-----
listas -> {listas}
-----
listas_anidadas -> {listas_anidadas}
-----""")