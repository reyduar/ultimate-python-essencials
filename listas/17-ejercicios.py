# pprint es una función que imprime diccionarios de forma ordenada
from pprint import pprint

# 1. Eliminar los espacios en blanco de un string, y devolver una lista con los caracteres resultantes.


def quitar_espacios_strip(string):
    return string.strip()


def quitar_espacios_replace(string):
    return string.replace(' ', '')


def quitar_espacios_join(string):
    return ''.join(string.split())


string = '  Holaaaaaa Mundo oooo '


def quitar_espacios(string):
    return [char for char in string if char != " "]


sin_espacios = quitar_espacios(string)
print(sin_espacios)  # ['H', 'o', 'l', 'a', 'M', 'u', 'n', 'd', 'o']

# 2. Contar en un diccionario la cantidad de veces que se repite cada caracteres en un string.


def contar_caracteres(lista):
    diccionario = {}
    for char in lista:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario


# {'H': 1, 'o': 2, 'l': 1, 'a': 1, 'M': 1, 'u': 1, 'n': 1, 'd': 1}
contar_caracteres = contar_caracteres(sin_espacios)
pprint(contar_caracteres, width=1)

# 3. Ordenar las llaves de un diccionario por el valor que tiene y devolver una lista que contienen tuplas


def ordenar_diccionario_des(diccionario):
    return sorted(diccionario.items(), key=lambda key: key[1], reverse=True)


ordenados = ordenar_diccionario_des(contar_caracteres)
# [('o', 2), ('H', 1), ('l', 1), ('a', 1), ('M', 1), ('u', 1), ('n', 1), ('d', 1)]
print(ordenados)

# 4. de un listado de tuplas, devolver las tuplas que tengan el mayor valor


def mayor_valor(tuplas):
    mayor = max(tuplas, key=lambda x: x[1])
    return [tupla for tupla in tuplas if tupla[1] == mayor[1]]


mayor_valor = mayor_valor(ordenados)
print(mayor_valor)  # [('o', 2)]

# 5. crear un mensaje que diga
# "El caracter que mas se repite es 'o' con 2 repeticiones"


def crear_mensaje(diccionario):
    mensaje = "El caracter que mas se repite son \n"
    for key, valor in diccionario.items():
        mensaje += f"{key} con {valor} repeticiones"
    return mensaje


# El caracter que mas se repite es 'o' con 2 repeticiones
print(crear_mensaje(contar_caracteres))
