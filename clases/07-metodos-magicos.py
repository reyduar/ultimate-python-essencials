class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def __del__(self):
        print(f'{self.nombre} ha sido eliminado')

    def __str__(self):
        return f'{self.nombre} es un {self.raza}'
        

    def ladrar(self):
        print(f'{self.nombre} está ladrando')


perro1 = Perro('Firulais', 'Pastor Alemán')
# Metodo mágico __str__ se ejecuta cuando se imprime un objeto
print(perro1) # perro1.__str__() 
text = str(perro1) # 
print(text) # Firulais es un Pastor Alemán

# Metodo mágico __del__ se ejecuta cuando se elimina un objeto
del perro1 # perro1.__del__()


#
# https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# https://docs.python.org/3/library/operator.html
# https://www.python-course.eu/python3_magic_methods.php
# https://realpython.com/operator-function-overloading/
# https://www.geeksforgeeks.org/operator-overloading-in-python/
# https://www.geeksforgeeks.org/magic-methods-python/
# https://www.geeksforgeeks.org/dunder-magic-methods-python/
# https://www.geeksforgeeks.org/str-vs-repr-in-python/


