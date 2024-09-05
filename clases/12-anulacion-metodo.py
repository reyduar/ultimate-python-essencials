class Ave:

    def __init__(self):
        self.volador = "Volador"

    def vuela(self):
        print("Ave Volando en los cielos")


class Pato(Ave):

    def __init__(self):
        # super() llama al constructor de la clase padre
        super().__init__()
        self.nadador = "Nadador"

    def vuela(self):
        print("Pato volando en los cielos")

# anulacion del metodo es cucando ponemos un metodo con el mismo nombre en la clase hija

pato = Pato()
pato.vuela()
print(pato.volador, pato.nadador)
