conjunto1 = {'uno', 'dos', 'tres'}
conjunto2 = {'bat', 'dos', 'hiru'}
fusion = conjunto1 | conjunto2
solo_en_uno = conjunto1 - conjunto2
ambos = conjunto1 & conjunto2
print(f"""
conjunto1 = {'uno', 'dos', 'tres'}
conjunto2 = {'bat', 'dos', 'hiru'}
Fusionar conjuntos, omitiendo elemento duplicado
fusion = conjunto1 | conjunto2 -> {fusion}
-----
etiquetas sólo en uno de los conjuntos
solo_en_uno = conjunto2 - conjunto1 -> {solo_en_uno}
-----
etiquetas en ambos conjuntos
ambos = conjunto1 & conjunto2 -> {ambos}
""")
