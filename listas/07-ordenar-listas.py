mascotas = ['perro', 'gato', 'pez', 'loro']

# Ordenar la lista
mascotas.sort()
print(mascotas)  # ['gato', 'loro', 'pez', 'perro']

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Ordenar la lista en reversa
mascotas.sort(reverse=True)
print(mascotas)  # ['perro', 'pez', 'loro', 'gato']

# Ordenar la lista con sorted
mascotas = ['perro', 'gato', 'pez', 'loro']
ordenada = sorted(mascotas)
print(ordenada)  # ['gato', 'loro', 'pez', 'perro']
print(mascotas)  # ['perro', 'gato', 'pez', 'loro']

# Ordenar la lista con sorted en reversa
ordenada = sorted(mascotas, reverse=True)
print(ordenada)  # ['perro', 'pez', 'loro', 'gato']
print(mascotas)  # ['perro', 'gato', 'pez', 'loro']

usuarios = [
    ['jose', 24],
    ['maria', 30],
    ['pedro', 20],
    ['ana', 25]
]

# Ordenar la lista de listas por la edad
usuarios.sort(key=lambda x: x[1])
print(usuarios)  # [['pedro', 20], ['jose', 24], ['ana', 25], ['maria', 30]]
usuarios.sort(key=lambda x: x[0])
print(usuarios)  # [['ana', 25], ['jose', 24], ['maria', 30], ['pedro', 20]]

# Ordenar la lista de listas por la edad en reversa
usuarios.sort(key=lambda x: x[1], reverse=True)
print(usuarios)  # [['maria', 30], ['ana', 25], ['jose', 24], ['pedro', 20]]

# Ordenamos la lista desde una funcion


def ordenar(usuario):
    return usuario[1]


usuarios.sort(key=ordenar)
print(usuarios)  # [['pedro', 20], ['jose', 24], ['ana', 25], ['maria', 30]]
