def sayHi():
    print("Hola, ¿cómo estás?")


sayHi()


def sayHello(name, apellido="no tiene"):
    print(f"Hola, {name}")
    print(f"Tu apellido es {apellido}")


sayHello("Juan")
sayHello("Juan", "Pérez")
sayHello(apellido="Duarte", name="Ariel")
