cadena = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
numeros = [1, 2, 3, 4, 5]
combinada = ['uno', 43, 1.5]
listas = [['uno', 'dos', 'tres', 'cuatro', 'cinco'], [1, 2, 3, 4, 5], 'listas anidadas']
listas_anidadas = [cadena, numeros, 'listas anidadas']

print(f"""
diferentes listas
listas combinadas son punogrosas por si hay funciones en bucle
listas anidadas, pueden contener otras listas como elemento
-----
cadena = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
cadena -> {cadena}
-----
numeros = [1, 2, 3, 4, 5]
numeros -> {numeros}
-----
combinada = ['uno', 43, 1.5]
combinada -> {combinada}
-----
listas = [['uno', 'dos', 'tres', 'cuatro', 'cinco'], [1, 2, 3, 4, 5], 'listas anidadas']
listas -> {listas}
-----
listas_anidadas = [cadena, numeros, 'listas anidadas']
listas_anidadas -> {listas_anidadas}
-----""")