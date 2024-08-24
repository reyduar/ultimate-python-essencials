mascotas = ['perro', 'gato', 'pez', 'loro']
mascotas.append('conejo')
print(mascotas)  # ['perro', 'gato', 'pez', 'loro', 'conejo']
mascotas.insert(2, 'hamster')
print(mascotas)  # ['perro', 'gato', 'hamster', 'pez', 'loro', 'conejo']

mascotas.remove('pez')
print(mascotas)  # ['perro', 'gato', 'hamster', 'loro', 'conejo']

mascotas.pop(2)
print(mascotas)  # ['perro', 'gato', 'loro', 'conejo']

print(mascotas.index('loro'))  # 2

print(mascotas[2:4])  # ['loro', 'conejo']

print(mascotas[:3])  # ['perro', 'gato', 'loro']

print(mascotas[2:])  # ['loro', 'conejo']

print(mascotas[1::2])  # ['gato', 'conejo']


numeros = list(range(1, 22))
# quiero los numeros impares
print(numeros[::2])  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# quiero los numeros pares
print(numeros[1::2])  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
