rangos = ['instagram', 'hades', 'rottweiler']
rangos_lista = rangos[1:2]
rangos_lista_final = rangos[1:]
rangos_lista_inicio = rangos[:2]
rangos_lista_sin_ultima = rangos[:-1]
rangos_lista_completa = rangos[:]
print(f"""range -> rango, coger solo unos cuantos elementos
-----
rangos = ['instagram', 'hades', 'rottweiler']
-----
rangos_lista = rangos[1:2] desde index hasta no incluido
{rangos_lista}
-----
rangos_lista_final = rangos[1:] desde index hasta final
{rangos_lista_final}
-----
rangos_lista_inicio = rangos[:2]desde inicio hasta no incluido
{rangos_lista_inicio}
-----
rangos_lista_sin_ultima = rangos[:-1] desde inicio hata index negativo
{rangos_lista_sin_ultima}
-----
rangos_lista_completa = rangos[:] lista completa
{rangos_lista_completa}
-----
""")