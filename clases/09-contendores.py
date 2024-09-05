class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} pesos"
    
class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def imprmir_productos(self):
        for producto in self.productos:
            print(producto)

producto1 = Producto('Laptop', 20000)
producto2 = Producto('Mouse', 500)
producto3 = Producto('Teclado', 1000)

categoria1 = Categoria('tecnologia', [producto1, producto2])
categoria1.agregar_producto(producto3)

categoria1.imprmir_productos()
