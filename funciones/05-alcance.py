saludo = "No hay saludo"  # Variable global


def sayHello(name):
    global saludo
    saludo = "Hola, " + name
    print(saludo)


def sayBye(name):
    saludo = "Adiós, " + name
    print(saludo)


sayHello("Juan")  # Hola, Juan
sayBye("Juan")  # Adiós, Juan
print(saludo)  # Hola, Juan
