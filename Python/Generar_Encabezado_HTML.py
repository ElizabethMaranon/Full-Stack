def generador(título, tipo):
  return f'<h{tipo}>{título}</h{tipo}>'
print(f"""
generador_encabezado(título, tipo)
automatizará la creación del encabezado mediante la interpolación
-----
función a programar 
def generador(título, tipo):
  return f'<h{{tipo}}>{{título}}</h{{tipo}}>'

{{generador('Encabezado1', '1')}} -> {generador('Encabezado1', '1')}
{{generador('lo que quieras', '5')}} -> {generador('lo que quieras', '5')}

""")

