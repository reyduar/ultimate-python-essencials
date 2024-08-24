
print("Bienvenido a la calculadora")
print("Opciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

opcion = ""
while opcion != "5":
    opcion = input(">")
    if opcion == "1":
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        print(numero1 + numero2)
    elif opcion == "2":
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        print(numero1 - numero2)
    elif opcion == "3":
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        print(numero1 * numero2)
    elif opcion == "4":
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        print(numero1 / numero2)
    elif opcion == "5":
        print("Adios")
    else:
        print("Opción inválida")
