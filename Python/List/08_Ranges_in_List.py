print('''range-> rango, coger solo unos cuantos elementos''')
print('''-----''')
print('''rangos = ['instagram', 'hades', 'rottweiler']''')
print('''-----''')
rangos = ['instagram', 'hades', 'rottweiler']
rangos_lista = rangos[1:2]
print('rangos_lista = rangos[1:2] desde index hasta no incluido')
print(rangos_lista)
print('''-----''')
rangos_lista_final = rangos[1:]
print('rangos_lista_final = rangos[1:] desde index hasta final')
print(rangos_lista_final)
print('''-----''')
rangos_lista_inicio = rangos[:2]
print('rangos_lista_inicio = rangos[:2]desde inicio hasta no incluido')
print(rangos_lista_inicio)
print('''-----''')
rangos_lista_sin_ultima = rangos[:-1]
print('rangos_lista_sin_ultima = rangos[:-1] desde inicio hata index negativo')
print(rangos_lista_sin_ultima)
print('''-----''')
print('rangos_lista_completa = rangos[:] lista completa')
rangos_lista_completa = rangos[:]
print(rangos_lista_completa)