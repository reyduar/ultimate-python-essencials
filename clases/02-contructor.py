class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f'{self.nombre} está ladrando')


perro1 = Perro('Firulais', 'Pastor Alemán')
perro2 = Perro('Rex', 'Doberman')

perro1.ladrar()  # Firulais está ladrando
perro2.ladrar()  # Rex está ladrando
