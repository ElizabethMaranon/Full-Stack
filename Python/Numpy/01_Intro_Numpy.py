"""
Instalar primer paquete de Python
Usar biblioteca Numpy (permite procesar, números, registros y objetos)
url:https://pypi.org/
buscar paquete que queramos, en este caso Numpy,
abrir terminal y ejecutar -> pip install numpy """

"""Sistema que toma números y de ese número,
crea un número variable de elementos de la lista"""

"""Importamos la biblioteca y le ponemos un alias"""
import numpy as np
"""Arange -> adelantar un número
y el número (cantidad) genera un rango con matriz (Similar a una lista)
16, empieza desde 0 hasta 15"""
rango_num = np.arange(16)
print(rango_num)
"""Ya tenemos la matriz creada de 0 a 15"""
"""Reshape -> Pasa dos números a la vez
obtenemos un conjunto anidado con cuatro matrices anidadas
dentro de la matriz maestra, cada una con 4 elementos"""
rango_num.reshape(4, 4)

"""Revisar la biblioteca numpy para ir conociendo funciones"""

