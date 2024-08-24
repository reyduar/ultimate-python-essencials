
usuarios = [
    ['jose', 24],
    ['maria', 30],
    ['pedro', 20],
    ['ana', 25]
]

# usar el operador map para obtener solo los nombres
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)  # ['jose', 'maria', 'pedro', 'ana']

# usar el operador filter para obtener solo los nombres que empiezan con 'm'
nombres_m = list(filter(lambda nombre: nombre.startswith('m'), nombres))
print(nombres_m)  # ['maria']

# usar el operador map para obtener los usuarios con m
usuarios_m = list(filter(lambda usuario: usuario[0].startswith('m'), usuarios))
print(usuarios_m)  # [['maria', 30]]
