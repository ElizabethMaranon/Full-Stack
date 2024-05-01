class alineación2: # Creamos la clase
    def __init__(self, jugadores):
        self.jugadores = jugadores       
    def linea(self):
        linea_max = len(self.jugadores) # Contador Jugadores
        index = 0       
        while True: # Bucle, mientras que
            if index < linea_max: # index sea menor que maximo de jugadores
                yield self.jugadores[index] 
            else: # Sino 
                index = 0 # index sea igual a 0
                yield self.jugadores[index]                
            index += 1 # Incrementar index en uno          
    def __repr__(self):
        return f'Alineación ({self.jugadores})'
    def __str__(self):
        return f"Alineacion con los jugadores: {', '.join(self.jugadores)}"
                        
equipo = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'] 

full_alineación2 = alineación2(equipo) # Creamos variable lista completa
equipo_linea = full_alineación2.linea() # Creamos ejemplo de líneas

print(next(equipo_linea))
print(next(equipo_linea))
print(next(equipo_linea))
print(repr(equipo_linea)) # return <generator object alineación2.linea at 0x000002008EB53850> por yield
print(str(equipo_linea)) # return <generator object alineación2.linea at 0x000002008EB53850> por yield