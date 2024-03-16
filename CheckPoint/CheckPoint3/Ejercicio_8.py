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