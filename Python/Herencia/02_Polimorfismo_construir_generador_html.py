class Html: # Creamos clase básica
    def __init__(self, contenido): # Atributos
        self.contenido = contenido # Creamos variable de instancia
        
    def render(self): # Nadie puede conectarse directamente, excepto hijos
        raise NotImplementedError('Subclass must implement render method') # Generar excepción o error
        
class encabezado(Html): # Creamos clase (heredada)
    def render(self): # Creamos función renderizada
        return f'<h1>{self.contenido}</h1>' # Devuelve cadena formateada
    
class div(Html): # Creamos clase (heredada)
    def render(self): # Creamos función renderizada
        return f'<div>{self.contenido}</div>' #devuelve cadena formateada
    
etiquetas = [ # Creamos los elementos de la variable
    div('Algún contenido'),
    encabezado('Algún encabezado bonito'),
    div('Otro contenido')
]

for etiqueta in etiquetas: # Iteramos a traves de nuestra lista
    print(str(etiqueta) + ':' + etiqueta.render())
    print(etiqueta.render())
