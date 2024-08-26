
class Perro:
    patas = 4

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def ladrar(cls):
        print('el perro está ladrando')
        
    @classmethod
    def factory(cls):
        return cls('Rex')

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


perro2 = Perro.factory()
print(perro2.nombre)  # Rex