priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))

diccionario = {
  (1, 'tupla1'): [1, 2, 3],
  (1, 'tupla2'): [11, 12, 13],
  (2, 'tupla3'): [21, 22, 23]
}
print(f"""
diccionario = {{
  (1, 'tupla1'): [1, 2, 3],
  (1, 'tupla2'): [11, 12, 13],
  (2, 'tupla3'): [21, 22, 23]
}}
variable es Diccionario
key/clave es tupla
value/valor es lista

print(list(diccionario.keys())) -> {list(diccionario.keys())}
print(list(diccionario.values())) -> {list(diccionario.values())}



""")