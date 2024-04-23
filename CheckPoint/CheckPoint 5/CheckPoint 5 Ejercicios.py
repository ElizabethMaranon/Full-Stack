print("""
Cree un bucle For de Python.
      """)
nums = [1, 2, 3]
for n in nums:
    print(n)
print("""-----
Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
      """)
"1ª opción"
a = 1
b = 2
c = 3
def suma(a, b, c):
  return a + b + c
print(suma(a, b, c))
"2 opción"
print(sum(nums))
print("""-----
Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
      """)
x = 1
y = 2
z = 3
sumar = lambda x,y,z : x + y + z
print(sumar(x,y,z))


print("""-----
Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
      """)
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'
nombre = 'Enrique'
if nombre in lista_nombre:
  print('El valor de la variable coincide')
else:
   print('El valor de la variable NO coincide')

print("""
*Sugerencia, si es necesario, utilice un bucle for in y el operador in.

      con bucle for in no sabría hacerlo.
      Agradecería ayuda """)

