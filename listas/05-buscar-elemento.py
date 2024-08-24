mascotas = ['perro', 'gato', 'pez', 'loro', 'perro']

# contar cuantas veces se repite un elemento
print(mascotas.count('perro'))  # 2

# Buscar un elemento en la lista
if 'perro' in mascotas:
    index = mascotas.index('perro')
else:
    print("No esta el perro")
