

import operator
from functools import reduce
print("""import operator
from functools import reduce
""")
print("""Entradas y salidas""")
print("""dynamic_reducer([1, 2, 3], '+') #6
dynamic_reducer([1, 2, 3], '-') #-4
dynamic_reducer([1, 2, 3], '*') #6
dynamic_reducer([1, 2, 3], '/') #0.16666666666666666""")



#Solucion
def dynamic_reducer(
    collection,
    op):  #definimos la funcion con los parametros de entrada y salida
  #creamos diccionario
  operators = {
      "+": operator.add,  #libreria.función
      "-": operator.sub,  #libreria.función
      "*": operator.mul,  #libreria.función
      "/": operator.truediv,  #libreria.función
  }
  #return funcion ((dos argumentos 1lambda total, elemento: nombre de nuesto dicciona[op](total, element)) 2collection)
  #primer elemento de lamdba es el total, el segundo es el elemento, le puedes llamar como tu quieras
  return reduce((lambda total, elemento: operators[op](total, elemento)),
                collection)


print(
    dynamic_reducer([1, 2, 3], '+')
)  #elementos serian 1, 2, 3 lo que corresponda que este dentro de la funcion
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))
