numero = 1

while numero <= 10:
    print(numero)
    numero += 1

comando = ""
while comando.lower() != "salir":
    comando = input(">")
    print("Escribiste", comando)
