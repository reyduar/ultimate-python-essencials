# multiple arguments

def suma1(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


def suma2(*numeros):
    print(sum(numeros))


suma2(1, 2, 3, 4, 5)  # 15
suma2(1, 2, 3)  # 6
suma1(1, 2)  # 3
