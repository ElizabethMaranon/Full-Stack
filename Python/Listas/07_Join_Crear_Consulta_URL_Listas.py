print(f"""
Resultado obtenido en la barra de dirección tras una busqueda
https://www.google.com/search?q=instagram+hades+rottweiler&rlz=1C1CHBD_esES964ES964&oq=instagram+hades+rottweiler&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg80gEKMjM1MTBqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8
eliminamos los datos que son exclusivo de google
uri es similar a url
https://www.google.com/search?q=instagram+hades+rottweiler
-----""")
uri = 'https://www.google.com/search?q='
busqueda = ['instagram', 'hades', 'rottweiler']
print(f"""uri = 'https://www.google.com/search?q='
busqueda = ['instagram', 'hades', 'rottweiler']
-----""")
busqueda_join = '+'.join(busqueda)
print(f"""Lo que queramos usar para unir se coloca dentro de comillas
busqueda_join = '+'.join(busqueda)
print(busqueda_join) -> {busqueda_join}
-----""")
busqueda_uri = f'{uri}{busqueda_join}'
print(f"""Usamos interpolation
busqueda_uri = f'{{uri}}{{busqueda_join}}' -> {busqueda_uri}
-----""")