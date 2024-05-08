def Precios(precio_bruto, extension): # Función para que cuando se llame se pase un valor bruto
    if isinstance(extension, int): #int() devuelve un número entero
        extension = extension * 0.01 # Pasar numero entero a decimal

    return int(precio_bruto) + extension


print(Precios(3.20, 99))
print(Precios(3.20, 0.99))
print(Precios(3.20, 0.20))
print(Precios(3.20, 20))
print(Precios(3, 95))
print(Precios(3, 0.95))

