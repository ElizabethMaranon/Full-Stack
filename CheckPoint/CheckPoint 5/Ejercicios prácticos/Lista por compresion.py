numeros = [1, 2, 3, 4] # lista de números
numeros_mas_uno = [] # nueva lista
for n in numeros: # for variable_bloque in nombre_lista
    numeros_mas_uno.append(n + 1) # añadir uno a cada numero de la lista
    
print(numeros_mas_uno)

numeros = [1, 2, 3, 4] # lista de números
comprension = [n + 1 for n in numeros] # lista = bloque + 1 for variable_bloque in nombre_lista 

print(comprension)