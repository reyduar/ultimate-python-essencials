# diccionarios en python son colecciones desordenadas de elementos indexados que se escriben entre llaves {}.

# Crear un diccionario
usuario = {
    "nombre": "jose",
    "edad": 24,
    "email": "jsmith@gmail.com",
    "activo": True,
    "amigos": ["maria", "pedro", "ana"]
}

# Acceder a un valor
print(usuario["nombre"])  # jose
print(usuario["edad"])  # 24
print(usuario["email"])  #
print(usuario["activo"])  # True

# Acceder a un valor con get
print(usuario.get("nombre"))  # jose
print(usuario.get("edad"))  # 24

# Acceder a un valor que no existe
print(usuario.get("telefono"))  # None

# Acceder a un valor que no existe con un valor por defecto
print(usuario.get("telefono", "No existe"))  # No existe

# Encontrar valores con if in
if "nombre" in usuario:
    print("El nombre es", usuario["nombre"])  # El nombre es jose

# Cambiar un valor
usuario["nombre"] = "pedro"
print(usuario["nombre"])  # pedro

# Agregar un valor
usuario["telefono"] = "123456789"
print(usuario["telefono"])  # 123456789

# Eliminar un valor
usuario.pop("telefono")
print(usuario.get("telefono"))  # None

# Eliminar un valor con del
del usuario["nombre"]
print(usuario.get("nombre"))  # None

# Recorrer un diccionario
for key in usuario:
    print(key, ":", usuario[key])  # edad : 24

# Recorrer un diccionario con items
for key, value in usuario.items():
    print(key, ":", value)  # edad : 24

# Recorrer un diccionario con keys
for key in usuario.keys():
    print(key, ":", usuario[key])  # edad : 24
