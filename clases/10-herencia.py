class Animal:
    def respirar(self):
        print('Respirar')

    def comer(self):
        print('Comer')
# Ejemplo de herencia
class Perro(Animal):
    def aullar(self):
        print('Aullar')

class Lobo(Animal):
    def cazar(self):
        print('Cazar')

    def aullar(self):
        print('Aullar')

# Herencia múltinivel
class Leon(Lobo):
    def rugir(self):
        print('Rugir')

perro = Perro()
perro.respirar()
perro.comer()

lobo = Lobo()
lobo.respirar()
lobo.comer()

leon = Leon()
leon.respirar()
leon.comer()
leon.cazar()
leon.rugir()

