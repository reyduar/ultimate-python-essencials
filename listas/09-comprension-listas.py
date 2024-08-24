usuarios = [
    ['jose', 24],
    ['maria', 30],
    ['pedro', 20],
    ['ana', 25]
]

nombres = [usuario[0] for usuario in usuarios]
print(nombres)  # ['jose', 'maria', 'pedro', 'ana']

edades = [usuario[1] for usuario in usuarios]
print(edades)  # [24, 30, 20, 25]

# Filtrar los nombres que empiezan con 'm'
nombres_m = [usuario[0] for usuario in usuarios if usuario[0].startswith('m')]
print(nombres_m)  # ['maria']
