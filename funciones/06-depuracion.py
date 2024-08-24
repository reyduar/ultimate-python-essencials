def largo(texto):
    resultado = 0
    for _ in texto:  # _ is a common name for a variable that is not used
        resultado += 1
    return resultado


l = largo("hola mundo")
print(l)
