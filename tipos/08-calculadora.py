entrada1 = input("Digite o primeiro número: ")
entrada2 = input("Digite o segundo número: ")
numero1 = int(entrada1)
numero2 = int(entrada2)
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

message = f""""
Para los números {numero1} y {numero2}:
- La suma es: {soma}
- La resta es: {subtracao}
- La multiplicación es: {multiplicacao}
- La división es: {divisao}
"""
print(message)
