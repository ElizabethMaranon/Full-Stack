diccionario = [
  {
    'primero': {
        'uno' : 'bat',
        'dos' : 'bi',
        'tres' : 'tres'
    }
  },
  {
    'segundo' : {
        'diez' : 'hamar',
        'veinte' : 'hogei',
        'treinta' : 'hogeitahamar'
    }
  }
]
diccionario_primero = diccionario[0].get('primero', 'Diccionario no encontrado')
print(f'''
Diccionarios dentro de un lista
Importante apertura y cierre de corchetes
Usar coma para separar valores, diccionarios, ....
-----
diccionario = [
  {{'primero': {{'uno' : 'bat', 'dos' : 'bi', 'tres' : 'tres'}}}},
  {{'segundo' : {{'diez' : 'hamar', 'veinte' : 'hogei', 'treinta' : 'hogeitahamar'}}}}
]
{diccionario}
-----
{diccionario_primero}
''')