for numero in range(10):
    print(numero, numero * 'hola mundo')


buscar = 11

for numero in range(10):
    if numero == buscar:
        print("Encontrado", numero)
        break
else:
    print("No encontrado", buscar)
