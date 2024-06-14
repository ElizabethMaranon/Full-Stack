"""
while
bucle infinito, hay que decirle que se detenga
se usa cuando no está claro el valor final
valor centinela, establecer valor para fin bucle"""
nums = list(range(1, 100))
print("""nums = list(range(1, 100)) #hace una lista desde, hasta
      """)
print(nums)

print("""-----""")
"""
Mientras la longitud de nums sea mayor que 0, imprimir.
Pop eliminara del diccionario por lo que ira definiendo el centinela
"""
while len(nums) >0:
  print(nums.pop())
print(f"""-----
Juego de memoria
while seguira ejecutandose hasta llegar al valor centinela
""")
def juego_memoria(): # creamos la función
  while True: # al ejecutarla
    print('cual es el resultado?')
    memoria = input()

    if memoria == '42': # valor centinela cuando se adivine
      print('Bingo') 
      return False # Detener el bucle
    else:
      print(f"El {memoria} no es correcto, inténtalo otra vez\n")
      # Cuando no se acierta, bucle

juego_memoria()

def loop_using_while():
    dog_house = ['1', '2', '3', '4'] # Put dog names here
    counter = 0
    while counter < len(dog_house):
        print(dog_house[counter])
        counter +=1
    
    return [dog_house, counter]
print(f"""
Coding Exercise

In the below starter code, place 4 dog names (elements) of your choice in the dog_house list. Then write a while loop that iterates through the dog_house list and prints each dogs name. An iterator variable named "counter" must be set, and must have an initial value of 0.
Hint: An iterator value (also sometimes called a sentinel value) is a value that exists outside of your loop, and that you update or otherwise keep track of each time you loop, so that your while loop knows when to end.
Example:
iterator_value = 0
while iterator_value < 10:
    print("Keep looping...")
    iterator_value += 1
      
dog_house = ['1', '2', '3', '4'] # Put dog names here
    counter = 0
    while counter < len(dog_house):
        print(dog_house[counter])
        counter +=1""")
