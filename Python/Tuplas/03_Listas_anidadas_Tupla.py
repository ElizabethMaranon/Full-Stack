Zenbakiak = ('Bat', 'Bi', 'Hiru')

print(f"""
Zenbakiak = ('Bat', 'Bi', 'Hiru')
      Index -1 1 -> {Zenbakiak[-1][1]}
      
Añadimos usando variable.
Recordar poner ',' al final
zenbakiak = ['Lau', 'Bost', 'Sei']
Zenbakiak += (zenbakiak,)""")
zenbakiak = ['Lau', 'Bost', 'Sei']
Zenbakiak += (zenbakiak,)
print(f"""
Directamente añadiendo la lista.
Recordar poner',' al final
Zenbakiak += (['Zaspi, Zortzi'],)""")
Zenbakiak += (['Zaspi, Zortzi'],)
print(f"""
Tupla actualizada - > {Zenbakiak}""")
print(f"""
Index 1 -> {Zenbakiak[1]}
Index -1 -> {Zenbakiak[-1]}
Index -1 -1 -> {Zenbakiak[-1][-1]}
Rango 1:2 -> {Zenbakiak[1:2]}
""")

