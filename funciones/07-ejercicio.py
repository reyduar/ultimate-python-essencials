def no_espacios(palabra):
    nueva_palabra = ""
    for letra in palabra:
        if letra != " ":
            nueva_palabra += letra
    return nueva_palabra


def reverse(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    return palabra_invertida


def es_palindramo(palabra):
    palabra = no_espacios(palabra)
    print(f"La palabra es: {palabra}")
    palabra_invertida = reverse(palabra)
    print(f"La palabra invertida es: {palabra_invertida}")
    if palabra == palabra_invertida:
        print("Es palindramo")
    else:
        print("No es palindramo")


es_palindramo("anita lava")
es_palindramo("anita lava la tina")
