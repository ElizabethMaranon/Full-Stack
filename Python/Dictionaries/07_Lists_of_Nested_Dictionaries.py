lista = [
  {
    'dic_primero': {
        'uno' : 'bat',
        'dos' : 'bi',
        'tres' : 'tres'
    }
  },
  {
    'dic_segundo' : {
        'diez' : 'hamar',
        'veinte' : 'hogei',
        'treinta' : 'hogeitahamar'
    }
  }
]

lista_dic_segundo = lista[1].get('dic_segundo', 'lista no encontrado')

print(f'''
Diccionarios dentro de un lista
Importante apertura y cierre de corchetes
Usar coma para separar valores, listas, ....
-----
lista = [
  {{'dic_primero': {{'uno' : 'bat', 'dos' : 'bi', 'tres' : 'tres'}}}},
  {{'dic_segundo' : {{'diez' : 'hamar', 'veinte' : 'hogei', 'treinta' : 'hogeitahamar'}}}}
]
Imprimir lista
print(lista) -> {lista}
-----
Devuelve values, con get aseguramos que la key esté
lista_dic_segundo = lista[1].get('dic_segundo', 'lista no encontrado')
{lista_dic_segundo}

Devuelve objeto de vista
{lista_dic_segundo.values()}

Convertir objeto de vista en lista
{list(lista_dic_segundo.values())}

Podemos tratarlo como una lista y buscaría index del valor deseado
{{list(lista_dic_segundo.values())[1]}} -> {list(lista_dic_segundo.values())[1]}
{{list(lista_dic_segundo.values())[0]}} -> {list(lista_dic_segundo.values())[0]}

''')