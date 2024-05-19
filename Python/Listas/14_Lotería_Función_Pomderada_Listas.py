import numpy as np
print(f'''
biblioteca -> import numpy as np
Sistema de juego para que la casa gane la mayoría de las veces''')
def loteria(resultado):
    lista_resultado =[]

    for (nombre, probabilidad) in resultado.items():
        for _ in range(probabilidad):
            lista_resultado.append(nombre)
    return np.random.choice(lista_resultado)

resultado = {
    'Has ganado el premio grande': 1,
    'Te ha tocado lo jugado': 2,
    'Lo siento, perdiste': 3
}
print(f'''
resultado = {{
    'Has ganado el premio grande': 1,
    'Te ha tocado lo jugado': 2,
    'Lo siento, perdiste': 3
}}
      
Función ->
    def loteria(resultado): 
    lista_resultado =[] 

    for (nombre, probabilidad) in resultado.items(): 
        for _ in range(probabilidad):
            lista_resultado.append(nombre)
        return np.random.choice(lista_resultado)
      
np.random.choice -> aleatorio el resultado
return(lista_resultado) imprime lista de resultados ['ganar', 'empatar', 'empatar', 'perder', 'perder', 'perder']

Run Python File y veremos si te ha tocado la loteria
Que tengas buena suerte
      
      {loteria(resultado)}
''')
