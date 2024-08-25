# operador de desempaquetar en python es un operador que permite desempaquetar los elementos de una lista, tupla, diccionario o set en variables individuales.

# Desempaquetar una lista
lista1 = [1, 2, 3]

lista2 = [4, 5, 6]

lista_unida = [*lista1, *lista2]
print(lista_unida)  # [1, 2, 3, 4, 5, 6]

# Desempaquetar un diccionario
diccionario1 = {'a': 1, 'b': 2, 'c': 'hola'}
diccionario2 = {'c': 3, 'd': 4, 'e': 'mundo'}
nuevo_diccionario = {**diccionario1, **diccionario2}
print(nuevo_diccionario)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 'mundo'}
