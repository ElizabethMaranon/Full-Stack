principio, centro, final = [1, 2, 3]
principio, *envoltura, final = [1, 2, 3, 4, 5]
print(f"""
envolver varios elementos en una sola variable
      
principio, centro, final = [1, 2, 3]
principio -> {principio}
centro -> {centro}
final -> {final}

principio, *envoltura, final = [1, 2, 3, 4, 5]
principio -> {principio}
envoltura -> {envoltura}
final -> {final}
-----""")
lista = ['<h1>', 'Título', 'Sub-Título', 'Contenido', '</h1>']
def eliminar_primero_y_último(lista_eliminados):
  _, *Contenido, _ = lista_eliminados
  return Contenido
print(f"""Elementos que queramos escribir con _ para eliminar
lista = ['<h1>', 'Título', 'Sub-Título', 'Contenido', '</h1>']
def eliminar_primero_y_último(lista_eliminados):
  _, *Contenido, _ = lista_eliminados
  return Contenido
print(eliminar_primero_y_último(lista)) -> {eliminar_primero_y_último(lista)}
-----""")
lista2 = ['', 'Título', 'Sub-Título', 'Contenido', '/' ]
print(f"""lista2 = ['', 'Título', 'Sub-Título', 'Contenido', '/' ]
print(eliminar_primero_y_último(lista2)) -> {eliminar_primero_y_último(lista2)}
""")

