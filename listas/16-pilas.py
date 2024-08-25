# pilas en python son colecciones ordenadas de elementos que se escriben entre corchetes [] y se pueden modificar.
pila = []
# Agregar un elemento al final
pila.append('a')
pila.append('b')
print(pila)  # ['a', 'b']

# Agregar un elemento al principio
pila.insert(0, 'z')
print(pila)  # ['z', 'a', 'b']

# Eliminar un elemento al final
pila.pop()
print(pila)  # ['z', 'a']

# Eliminar un elemento al principio
pila.pop(0)
print(pila)  # ['a']

# preguntar si la pila esta vacia
if not pila:
    print('La pila esta vacia')  # La pila esta vacia
