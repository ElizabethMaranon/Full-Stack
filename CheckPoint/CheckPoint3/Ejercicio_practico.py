#Ejercicio 1: Cree una cadena, un número, una lista y un valor booleano, cada uno almacenado en su propia variable.
cadena = 'Eli Marañon es Mielma'
número = 43
lista =[10, 20, 30, 40, 50]
valor_booleano = True
print(cadena)
print(número)
print(lista)
print(valor_booleano)

#Ejercicio 2: Utilice un índice para tomar las primeras 3 letras de su cadena y guárdelas en una variable.
frase = 'Eli Marañón es Mielma'
letras = frase[0:3]
print(frase)
print(letras)

#Ejercicio 3: Utilice un índice para tomar el primer elemento de su lista.
#Sin crear una nueva variable
lista = ['Eli', 'Hades', 'Ivan']
print(lista[0])
#Creando una nueva variable
lista0 = lista[0]
print(lista0)

#Crea una nueva variable numérica que sume 10 a tu número original.
numero = 7
nuevo_numero = 10 + numero
print(nuevo_numero)

#Ejercicio 5: Utilice un índice para obtener el último elemento de su lista.
#Sin crear una nueva variable
lista = ['Eli', 'Hades', 'Ivan']
print(lista[-1])
#Creando una nueva variable
listafin = lista[-1]
print(listafin)

#Ejercicio 6: Utilice dividir para transformar la siguiente cadena en una lista.
nombres = 'harry,alex,susie,jared,gail,conner'
lista_nombres = nombres.split(',')
print(lista_nombres)

#Ejercicio 7: Obtenga la primera palabra de su cadena usando índices.
#Utilice la función superior para transformar las letras en mayúsculas.
#Cree una nueva cadena que tome la palabra en mayúscula y el resto de la cadena original.
frase = 'eli marañón es mielma'
print(frase[0:3])
print(frase[0:3].upper())
Frase = frase[0:3].upper() + frase[3:]
print(Frase)

#Ejercicio 8: Utilice la interpolación de cadenas para imprimir una oración que contenga su variable numérica.
producto = 'Full Stack'
nombre = 'Mielma Developer'
fundacion = 'FundaciónVass'
edad = 43
interpolacion = f'''
Hola {fundacion}:
El aprendizaje {producto} lo estoy cursando a la edad de {edad}.
Lo estoy disfrutando.
Atentamente, {nombre}
'''
print(interpolacion)

#Ejercicio 9: Imprime "hola mundo".
print('hola mundo')

# Además necesito que me crees una cadena que contenga la palabra "Hola".
string = 'Saludé diciendo Hola'
# Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena.
busqueda = string.find('Hola')
print(busqueda)
# Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
string = string.replace('Hola', 'adiós')
print(string)
