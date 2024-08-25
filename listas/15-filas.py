# filas en python son colecciones ordenadas de elementos que se escriben entre corchetes [] y se pueden modificar.
from collections import deque
# Crear una fila
fila = deque(['a', 'b', 'c', 'd'])
print(fila)  # deque(['a', 'b', 'c', 'd'])

# Agregar un elemento al final
fila.append('e')
print(fila)  # deque(['a', 'b', 'c', 'd', 'e'])

# Agregar un elemento al principio
fila.appendleft('z')
print(fila)  # deque(['z', 'a', 'b', 'c', 'd', 'e'])

# Eliminar un elemento al final
fila.pop()
print(fila)  # deque(['z', 'a', 'b', 'c', 'd'])

# Eliminar un elemento al principio
fila.popleft()
print(fila)  # deque(['a', 'b', 'c', 'd'])

# Eliminar todos los elementos
fila.clear()
print(fila)  # deque([])

# Crear una fila vacia
fila_vacia = deque()
