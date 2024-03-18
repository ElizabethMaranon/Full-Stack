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
