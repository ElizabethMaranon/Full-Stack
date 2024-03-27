elementos_anidados = {
    'primero': ['diez', 'once'],
    'segundo': ['veinte', 'veintiuno'],
    'tercero': ['treinta', 'treintayuno'],
    'cuarto': ['cuarenta', 'cuarentayuno']
}
del elementos_anidados['primero']
elementos_anidados.pop('Segundo', 'Clave no encontrada')
eliminar_KeyError = elementos_anidados.pop('Segundo', 'Clave no encontrada')
eliminar_tercero = elementos_anidados.pop('Tercero', 'Clave no encontrada')
eliminar_cuarto = elementos_anidados.pop('cuarto', 'Clave no encontrada' )

print(f'''
elementos_anidados = {{
    'primero': ['diez', 'once'],
    'segundo': ['veinte', 'veintiuno'],
    'tercero': ['treinta', 'treintayuno'],
    'cuarto': ['cuarenta', 'cuarentayuno']
}}
-----
Eliminar elementos del diccionario

-----

Del, forma mas básica
del elementos_anidados['primero'] -> elimina la key con sus correspondientes valores
{elementos_anidados}

del elementos_anidados['Segundo'] -> si la key no está, produce KeyError al imprimir para evitar usar pop
{elementos_anidados}

Imprime el diccionario sin dar error, pero sin saber si la clave fue correcta, crear variable para saber si está
eliminar_KeyError = elementos_anidados.pop('Segungo', 'Clave no encontrada')
{eliminar_KeyError}

Elimina la key y sus valores, guardando los valores en la nueva variable
Si la Key no estuviera, lanza mensaje elegido en pop
eliminar_tercero = elementos_anidados.pop('Tercero', 'Clave no encontrada')
{eliminar_tercero}
eliminar_cuarto = elementos_anidados.pop('cuarto', 'Clave no encontrada' )
{eliminar_cuarto}

Resultado
{elementos_anidados}


''')
