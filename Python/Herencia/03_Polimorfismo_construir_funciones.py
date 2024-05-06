class encabezado: # Creamos clase
    def __init__(self, contenido): # Atributos
        self.contenido = contenido # Creamos variable de instancia
    def render(self): # Creamos función renderizada
        return f'<h1>{self.contenido}</h1>' # Devuelve cadena formateada
    
class div: # Creamos clase
    def __init__(self, contenido): # Atributos
        self.contenido = contenido # Creamos variable de instancia
    def render(self): # Creamos función renderizada
        return f'<div>{self.contenido}</div>' #devuelve cadena formateada
    
div_uno = div('Algún contenido') # Creamos las variables
encabezado = encabezado('Algún encabezado bonito') # si colocas coma al final, python cree que es tupla
div_dos = div('Otro contenido')

def html_render(objeto): # Función render
    print(objeto.render())

html_render(div_uno)
html_render(encabezado)
html_render(div_dos)    
