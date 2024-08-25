# sets en python son colecciones desordenadas de elementos unicos y no indexados que se escriben entre llaves {}.
primer = {1, 2, 3, 4, 5}
print(primer)  # {1, 2, 3, 4, 5}

# Los sets no permiten elementos duplicados
segundo = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(segundo)  # {1, 2, 3, 4, 5}

# Crear un set vacio
tercer = set()
print(tercer)  # set()

# Crear un set con elementos
cuarto = set([1, 2, 3, 4, 5])
print(cuarto)  # {1, 2, 3, 4, 5}

# operadores sobre sets
# union (elementos que estan en ambos sets)
union = primer | segundo
print(union)  # {1, 2, 3, 4, 5}

# interseccion (elementos que estan en ambos sets)
interseccion = primer & segundo
print(interseccion)  # {1, 2, 3, 4, 5}

# diferencia (elementos que no estan en el primer set)
diferencia = primer - segundo
print(diferencia)  # set()

# diferencia simetrica (elementos que no estan en ambos sets)
primer = {1, 2, 3, 4, 5}
segundo = {5, 7, 8, 1, 10}
diferencia_simetrica = primer ^ segundo
print(diferencia_simetrica)  # {2, 3, 4, 7, 8, 10}
