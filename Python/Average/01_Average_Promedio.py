from functools import reduce # De la biblioteca importar función

def promedio(lista_num): # Crear función, no tiene que coincidir con el nombre de la lista
    
    total = reduce((lambda total, element: total + element), lista_números) # Función lambda suma num lista 
    
    return total / len(lista_num) # devuelve el total / cantidad números lista

lista_números = [1, 2, 3, 4, 5, 6] # Crear lista

print(promedio(lista_números)) # Imprimir Función promedio



