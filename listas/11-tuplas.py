
# A documentation comment is a way to provide information about the purpose and usage of a code snippet. In Python, a documentation comment is typically enclosed within triple quotes (""").


# A tuple in Python is an immutable sequence of elements, enclosed within parentheses (). It can contain elements of different data types and can be accessed using indexing or slicing.


numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)  # Output: (1, 2, 3, 4, 5, 6)

# The elements of a tuple can be accessed using indexing. The index of the first element is 0, the index of the second element is 1, and so on. Negative indexing can also be used to access elements from the end of the tuple.
punto = tuple([1, 2, 3])
print(punto[0])  # Output: 1

# The elements of a tuple can be accessed using slicing. Slicing allows you to access a subset of elements from the tuple. The syntax for slicing is tuple[start:stop:step].
numeros = (1, 2, 3, 4, 5, 6)
print(numeros[1:4])  # Output: (2, 3, 4)

primero, segundo, *otros = numeros
print(otros)  # Output: [3, 4, 5, 6]

# cast a tuple to a list
numeros = (1, 2, 3)
numeros_lista = list(numeros)
numeros_lista[0] = 4
print(numeros_lista)  # Output: [4, 2, 3]
