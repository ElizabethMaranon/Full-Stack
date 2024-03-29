print('''
Resultado obtenido en la barra de dirección tras una busqueda
https://www.google.com/search?q=instagram+hades+rottweiler&rlz=1C1CHBD_esES964ES964&oq=instagram+hades+rottweiler&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg80gEKMjM1MTBqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8
eliminamos los datos que son exclusivo de google
uri es similar a url
https://www.google.com/search?q=instagram+hades+rottweiler''')
print('''-----''')
print('''uri = 'https://www.google.com/search?q='
busqueda = ['instagram', 'hades', 'rottweiler']''')
uri = 'https://www.google.com/search?q='
busqueda = ['instagram', 'hades', 'rottweiler']
print('''-----''')
print('''Lo que queramos usar para unir se coloca dentro de comillas
busqueda_join = '+'.join(busqueda)
print(busqueda_join)''')
busqueda_join = '+'.join(busqueda)
print(busqueda_join)
print('''-----''')
print('''usamos interpolation
busqueda_uri = f'{uri}{busqueda_join}'
print(busqueda_uri)''')
busqueda_uri = f'{uri}{busqueda_join}'
print(busqueda_uri)
print('''-----''')