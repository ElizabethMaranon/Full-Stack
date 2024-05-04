
class Usuario: # Creamos una clase básica
    def __init__(self, email, nombre, apellido): # Tres atributos
        self.email = email # Creamos variable de instancia
        self.nombre = nombre # Creamos variable de instancia
        self.apellido = apellido # Creamos variable de instancia
        
    def saludo(self): # Agregamos comportamiento
        return f'Hola {self.nombre} {self.apellido}' # Devuelve cadena formateada
    
class Administrador(Usuario): # Creamos una clase heredada (la clase que va a heredar)
    def usuarios_activos(self): # Creamos la función
        return '500' #solo devolvemos número

Mielma = Administrador('mielma80@gmail.com', 'Mielma', 'Developer') # Creamos un administrador

Eli = Usuario('email@gmail.com', ' Eli', 'Marañón') # Creamos un usuario

print(Mielma.usuarios_activos()) # Nos devuelve la cantidad de usuarios activos que hay
print(Eli.usuarios_activos()) # AttributeError: 'Usuario' object has no attribute 'usuarios_activos'

