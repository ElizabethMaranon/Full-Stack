usuario = 'admin'
operador_ternario = 'acceso permitido' if usuario == 'admin' else 'acceso denegado'
print(f"""
Cuidado, es dificl de leer, puede crear erratas
Lo bueno es que esta el codigo en una sóla línea

Operador ternario
usuario = 'admin'
operador_ternario = 'acceso permitido' if usuario == 'admin' else 'acceso denegado'
admin tiene {operador_ternario}""")
usuario = 'invitado'
operador_ternario = 'acceso' if usuario == 'admin' else 'acceso denegado'
print(f"""
usuario = 'invitado'
operador_ternario = 'acceso' if usuario == 'admin' else 'acceso denegado'
invitado tiene {operador_ternario}""")
usuario = 'admin'
if usuario == 'admin':
  condicional = 'acceso permitido'
else:
  condicional = 'acceso denegado'
print(f"""
condicional normal
usuario = 'admin'
if usuario == 'admin':
  condicional = 'acceso permitido'
else:
  condicional = 'acceso denegado'
admin {condicional}
""")
print(f"""
Coding Exercise
Write a ternary operator that sets "language_check" to True if "language" is set as "python",
and sets it to False if it's not.

language = "python"

language_check = True if language == 'python' else False
""")