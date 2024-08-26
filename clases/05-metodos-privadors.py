
class Perro:

    def __init__(self, nombre, raza):
        self.__nombre = nombre # __ significa que el atributo es privado
        self.__raza = raza

    @classmethod
    def factory(cls):
        return cls('Rex', 'Caramelo')
    
    def ladrar(self):
        print(f'{self.__nombre} está ladrando {self.__raza}')

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        

   

perro2 = Perro.factory()
print(perro2.ladrar())
print(perro2.__dict__) # es para ver los nombre de nuestros atrubutos privados
print(perro2._Perro__nombre) # para acceder a los atributos privados