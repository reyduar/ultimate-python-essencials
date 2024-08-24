mascotas = ['perro', 'gato', 'pez', 'loro']

# agregar un elemento al final de la lista
mascotas.append('conejo')
print(mascotas)  # ['perro', 'gato', 'pez', 'loro', 'conejo']

mascotas.insert(2, 'hamster')  # insertar un elemento en la posicion 2
print(mascotas)  # ['perro', 'gato', 'hamster', 'pez', 'loro', 'conejo']

# eliminar un elemento de la lista
mascotas.remove('pez')
print(mascotas)  # ['perro', 'gato', 'hamster', 'loro', 'conejo']

# eliminar un elemento de la lista por su indice
mascotas.pop(2)
print(mascotas)  # ['perro', 'gato', 'loro', 'conejo']

# eliminar un elemento con del
del mascotas[1]
print(mascotas)  # ['perro', 'loro', 'conejo']

# eliminar todos los elementos de la lista
mascotas.clear()
print(mascotas)  # []
