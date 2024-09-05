class Volador:
    def volar(self):
        print("Volando")

class Nadador:
    def nadar(self):
        print("Nadando")

class Caminador:
    def caminar(self):
        print("Caminando")

class Pato(Volador, Nadador, Caminador):
    def cagar(self):
        print("Cagando")

pato = Pato()
pato.volar()
pato.nadar()
pato.caminar()
pato.cagar()