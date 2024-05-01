class alineación: # Creamos de clase
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.último_jugador_index = (len(self.jugadores) -1 ) # Creamos variable para refactorizar
    def __iter__(self):
        self.n = 0 
        return self 
    def get_jugador(self, n):
        return self.jugadores[n] # Creamos una nueva función
    def __next__(self): 
        if self.n < self.último_jugador_index: # Refactoriado
            jugador = self.get_jugador(self.n) # Nueva función
            self.n += 1 
            return jugador 
        elif self.n == self.último_jugador_index: # Refactoriado
            jugador = self.get_jugador(self.n) # Nueva función
            self.n = 0 
            return jugador
equipo = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'] 

equipo_alineación = alineación(equipo) 

process = iter(equipo_alineación) 
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
