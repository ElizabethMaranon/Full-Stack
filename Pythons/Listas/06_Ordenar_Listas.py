lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
enteros = [48, 2, 30, 7, 23, 28, 26]
flot = [1.25, 2.36, 1.25, 9.58, 0.11]
combi = [43, 1.25, 2/5, 4+6, 3*52]
print(f"""
Ordenar listas. Excepto combinados numero y string -> error
lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
enteros = [48, 2, 30, 7, 23, 28, 26]
flot = [1.25, 2.36, 1.25, 9.58, 0.11]
combi = [43, 1.25, 2/5, 4+6, 3*52]
-----""")
lista.sort()
enteros.sort()
flot.sort()
combi.sort()
print(f"""sort() -> orden a-z lista.sort()
lista.sort() -> {lista}
enteros.sort() -> {enteros}
flot.sort() -> {flot}
combi.sort() -> {combi}
-----""")
lista.sort(reverse=True)
enteros.sort(reverse=True)
flot.sort(reverse=True)
combi.sort(reverse=True)
print(f"""sort(reverse=True) -> orden z-a lista.sort(reverse=True)''')
lista.sort(reverse=True) -> {lista}
enteros.sort(reverse=True) -> {enteros}
flot.sort(reverse=True) -> {flot}
combi.sort(reverse=True) -> {combi}
-----""")