"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""
sales = {
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}
print(f"""
Crear diagramas sencillos
No se pueden hacer operaciones entre string y number,
excepción numero por string para que repita tantos como pidamos
-----
Si queremos 7 simbolos $
print(7 * '$') -> {7 * '$'}
-----
Ejercicio
Creamos un diccionario  
sales = {{
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}}
calculos necesarios a realizar
print(f'''
{{g sales['google'] * '$'}}
{{f sales['facebook'] * '$'}}
{{t sales['twitter'] * '$'}}
{{o sales['offline'] * '$'}}
''')
Resultado ->
{'g ' + sales['google'] * '$'}
{'f ' + sales['facebook'] * '$'}
{'t ' + sales['twitter'] * '$'}
{'o ' + sales['offline'] * '$'}
""")


