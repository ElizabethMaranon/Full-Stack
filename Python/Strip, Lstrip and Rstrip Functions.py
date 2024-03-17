strip = '''inicioprint(strip.strip())
elimina los espacios en blanco al inicio y al final de la cadena.final
'''
print(strip.strip())

strip_parentesis = '''inicioprint(strip_parentesis.strip('inicio'))
elimina los valores que esten entre parentesis.final'''
print(strip_parentesis.strip('inicio'))

lstrip = '''inicioprint(lstrip.lstrip('inicio'))
como strips, left (izquierda) pero elimina los valores desde la izquierda de la cadena hasta cumplir los valores de los parentesis.final'''
print(lstrip.lstrip('inicio'))

rstrip = '''inicioprint(rstrip.rstrip('final'))
como strips, right(derecha) pero elimina los valores desde la derecha la cadena hasta cumplir los valores de los parentesis.final'''
print(rstrip.rstrip('final'))

frase = 'https://mielma.es'
frase = frase.lstrip('https://')
frase = frase.rstrip('.es')
frase = frase.capitalize()
print(frase)
