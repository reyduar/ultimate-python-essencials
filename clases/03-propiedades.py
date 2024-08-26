
class Perro:
    patas = 4

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f'{self.nombre} está ladrando')

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza


Perro.patas = 3
perro1 = Perro('Firulais', 'Pastor Alemán')
perro2 = Perro('Rex', 'Doberman')
perro2.patas = 4
print(perro1.patas)  # 3
print(perro2.patas)  # 4
