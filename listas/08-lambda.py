usuarios = [
    ['jose', 24],
    ['maria', 30],
    ['pedro', 20],
    ['ana', 25]
]

# Ordenamos la lista desde una funcion sin lambda


def ordenar(usuario):
    return usuario[1]


usuarios.sort(key=ordenar)
print(usuarios)  # [['pedro', 20], ['jose', 24], ['ana', 25], ['maria', 30]]


# Ordenar con lambda
usuarios.sort(key=lambda usuario: usuario[1])
print(usuarios)  # [['pedro', 20], ['jose', 24], ['ana', 25], ['maria', 30]]
usuarios.sort(key=lambda usuario: usuario[0])
print(usuarios)  # [['ana', 25], ['jose', 24], ['maria', 30], ['pedro', 20]]
