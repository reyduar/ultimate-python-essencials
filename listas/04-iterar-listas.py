mascotas = ['perro', 'gato', 'pez', 'loro']

for mascota in mascotas:
    print(mascota)

# Usando enumerate para obtener el indice y el valor
for indice, mascota in enumerate(mascotas):
    # print(mascota)  # (0, 'perro') (1, 'gato') (2, 'pez') (3, 'loro')
    # print(indice)  # perro gato pez loro
    print(indice, mascota)  # 0 perro 1 gato 2 pez 3 loro
