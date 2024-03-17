meal_completed = True
total = 100
tip = total * 1/5
total = total + tip
receipt = "Your total is " + str(total)
print(receipt)

Comida_finalizada = True
subtotal = 100
propina = subtotal * 1/5
print(subtotal)
print(propina)
total = subtotal + propina
print(total)

variable_descriptiva = 'variable_descriptiva'
variable_python_serpiente = 'variable_python_serpiente'
variableJavaCamello = 'variableJavaCamello'
print(variable_descriptiva)
print(variable_python_serpiente)
print(variableJavaCamello)


Tipos_de_datos = 'Tipos de datos, Booleans, Numbers, Strings, Bytes, None, Arrays, Tuples, Sets, Dictionaries'
print(Tipos_de_datos)
print('Booleans (Verdadero o Falso)')
is_single = True
print(type(is_single))
print(is_single)
print('Numbers - Numeros')
enteros = 1
decimales = 0,11111223454366573452345
fracciones = 1/2
print(type(enteros))
print(enteros)
print(type(decimales))
print(decimales)
print(type(fracciones))
print(fracciones)
print('Strings - nombre, html, texto')
nombre = 'Nombre, html, texto...'
print(type(nombre))
print(nombre)
print('Bytes - Arrywebytes')
Proximamente = b'Proximamente'
print(type(Proximamente))
print(Proximamente)
print('None - nada, sin asignar dato')
Variable = None
print(type(Variable))
print(Variable)

print('Categoría de estructura de datos, Listas, Tuplas, Conjuntos, Diccionarios')
print('Arrays - listas inmutables')
lista = ['Nombre, html, texto...']
print(type(lista))
print(lista)
print('Tuples - tuplasmutable')
tupla = ('Nombre, html, texto...')
print(type(tupla))
print(tupla)
print('Sets - conjuntos')
conjunto = {'Nombre, html, texto...'}
print(type(conjunto))
print(conjunto)
print('Dictionaries - diccionarios mutables y no ordenados')
diccionario = {'Nombre, html, texto...'}
print(type(diccionario))
print(diccionario)

print('Comillas dobles o simples indistintamente, pero la misma al principio y al final')
sentence = 'the quick brown fox jumped over the lazy dog'
comillas = "the quick brown fox jumped over the lazy dog"
apostrofe_comillas = "cuando uses comillas dobles, apostofre don't"
print(apostrofe_comillas)
apostrofe_comilla = 'cuando uses comillas simples, apostofre don\'t'
print(apostrofe_comilla)
barra_invertida = "barra invertida anula la comilla simple o doble que se use dentro de la string"
print(barra_invertida)

sentence = 'the quick brown fox jumped over the lazy dog'.upper()
print("sentence = 'the quick brown fox jumped over the lazy dog.upper'()")
print(sentence)
print(sentence.upper()) 
print("sentence_dos = sentence.upper()")
sentence_dos = sentence.upper()
print(sentence_dos)

print('variable.lower() minuscula frase entera')
print(sentence.lower())
sentence = 'the Quick brown fox juMped over the lazy dog'
print(sentence)
print('variable.upper() mayuscula frase entera')
print(sentence.upper())
print('variable.capitalize() primera letra en mayuscula')
print(sentence.capitalize())
print('variable.title() primera letra de cada palabra en mayuscula')
print(sentence.title())
print('variable.lower() minuscula frase entera')
print(sentence.lower())

print('strings contar el primer caracter seria 0, el segundo 1, el tercero 2, etc')

sentence = 'The quick brown fox jumped over the lazy dog'
print('sentence[4] solo imprime el caracter especificado entre los corchetes')
print(sentence[4])

print('first_word = sentence[0:3] #rango cuenta hasta justo antes del caracter numerado')
print("new_sentence = 'Thy' + sentence[3:] #Rango a mantener, sin numero hasta es final")
new_sentence = 'Thy' + sentence[3:] #Rango a mantener, sin numero hasta es final
print(new_sentence)


print('Heredoc string multi-linea comillas triples')
content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""
print('.strip()elimina las lineas vacias del principio y del final que se generan por poner las triples comillas solas en una linea')
print(content)
print('repr(var)elimina los caracteres que el interpreta, por ejemplo enters y los devuelve con \n')
print(repr(content))

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'
print(long_string)
