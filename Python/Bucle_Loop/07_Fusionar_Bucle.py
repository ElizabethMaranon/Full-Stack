numeros = ['uno', 'dos']
zenbakiak = ['hiru', 'lau']
listas_en_lista = [numeros, zenbakiak]
for zenbakia in zenbakiak:
  numeros.append(zenbakia)
print(f"""
Crea una lista con las listas
numeros = ['uno', 'dos']
zenbakiak = ['hiru', 'lau']
listas_en_lista = [numeros, zenbakiak] -> {listas_en_lista}

Crea lista añadiendo elementos de una lista a otra 
for zenbakia in zenbakiak:
  numeros.append(zenbakia)
{numeros}
""")
numbers = [1,2,3,4,5,6]
result = []

for num in numbers:
    result.append(num + 1)
print(f"""
Coding Exercise
Write a for loop that takes each number from the numbers list,
increments it by 1, and adds it to the result list.

def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for num in numbers:
        result.append(num + 1)
    
    return result
{result}""")