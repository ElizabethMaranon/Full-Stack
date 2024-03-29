Zenbakiak = ('Bat', 'Bi', 'Hiru')
print(f"""
Agregar reasignando, identificador se ve que cambia la tupla
Zenbakiak = ('Bat', 'Bi', 'Hiru') -> {Zenbakiak}
id(zenbakiak) -> {id(Zenbakiak)}

Añadir ',' para que no sea string, sino tupla
Creamos una nueva tupla, anulando el nombre de la variable, dos maneras""")
Zenbakiak = Zenbakiak + ('Lau',)
print(f"""1º - Zenbakiak = Zenbakiak + ('Lau',) -> {Zenbakiak}
id(zenbakiak) -> {id(Zenbakiak)} """) 
Zenbakiak += ('Bost',)
print(f"""2º - Zenbakiak += ('Bost') -> {Zenbakiak}
id(zenbakiak) -> {id(Zenbakiak)} 

Desempaquetamos
Uno, Dos, Tres, Cuatro, Cinco = Zenbakiak""")
Uno, Dos, Tres, Cuatro, Cinco = Zenbakiak
print(f"""
{{Uno}} -> {Uno}
{{Dos}} -> {Dos}
{{Tres}} -> {Tres}
{{Cuatro}} -> {Cuatro}
{{Cinco}} -> {Cinco}
-----
""")
