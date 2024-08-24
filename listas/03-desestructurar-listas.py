numeros = [1, 2, 3, 4, 5]
# desestructurar la lista
uno, dos, tres, cuatro, cinco = numeros
print(uno)  # 1
print(dos)  # 2
print(tres)  # 3
print(cuatro)  # 4
print(cinco)  # 5

uno, dos, *resto = numeros
print(resto)  # [3, 4, 5]

primero, *resto, ultimo = numeros
print(resto)  # [2, 3, 4]
print(primero)  # 1
print(ultimo)  # 5
