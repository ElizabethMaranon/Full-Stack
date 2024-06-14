listas = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
"""Como cortar y continuar el bucle basado en una condición,
sin ser desde el principio hasta el final`
Tenemos dos operadores de flujo Continue / Break"""
print("""
Continue
""")
for lista in listas:
  if lista == 'cuatro': # Si encuentra la condición y es verdadera
    print(f"Lo siento {lista}, no estas incluido")
    continue # Le dice al programa que siga con el bucle
  else: # En caso contrario
    print(f"{lista}, estas incluido")
print("""-----
Break""")
for lista in listas:
  if lista == 'cuatro':
    print(f"{lista} tu index es {listas.index(lista)}")
    break # Le dice al programa que corte el bucle
  print(lista)

print(f"""
-----
Coding Exercise
      """)
"""Write a loop that loops over the list of vegetables and prints each one out.
When it reaches 'apple' it should print 'apple is not a vegetable' and then break.

def loop_and_break():
    vegetables = ["onion", "broccoli", "apple", "spinach"]
    for vegetable in vegetables:
        if vegetable == 'apple':
            print('apple is not a vegetable')
            break
        print(vegetable)
"""
vegetables = ["onion", "broccoli", "apple", "spinach"]
for vegetable in vegetables:
    if vegetable == 'apple':
        print('apple is not a vegetable')
        break
    print(vegetable)