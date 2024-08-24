# Ejericio de operadores lógicos con NOT
gas = True
encendido = False
edad = 55
if gas and not encendido and edad >= 18:
    print("El coche habilitado")
else:
    print("El coche deshabilitado")

# Ejericio de operadores lógicos con OR
encendido = True
edad = 17

if gas and (encendido or edad >= 18):
    print("El coche habilitado")
else:
    print("El coche deshabilitado")

# Ejericio de operadores lógicos con corto circuito
encendido = False
edad = 17

if gas and (encendido or edad >= 18):
    print("El coche habilitado")
else:
    print("El coche deshabilitado")
