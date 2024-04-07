lista = [0, 1, 2, 3, 4, 5, 6]
print(f"""
lista = [0, 1, 2, 3, 4, 5, 6]
-----
slice -> sector(fracción)
guardar sectores para usarlas mas tarde,
si hubiera que cambiar solo habria cambiamos la variable
-----""")
lista_corte = slice(2)
print(f"""
lista_corte = slice(2) -> slice(empieza, acaba, intervalo)
print(lista_corte) -> {lista_corte}
print(lista[lista_corte] -> {lista[lista_corte]})
-----""")
corte_variado = slice(1, 4, 2)
print(f"""corte_variado = slice(1, 4, 2)
print(lista[1:4:2]) -> {lista[1:4:2]}
print(lista[corte_variado]) -> {lista[corte_variado]}
-----""")
print(f"""Saber donde esta el rango de una variable
print(corte_variado.start) empieza -> {corte_variado.start}
print(corte_variado.stop) acaba -> {corte_variado.stop}
print(corte_variado.step) intervalo -> {corte_variado.step}
""")