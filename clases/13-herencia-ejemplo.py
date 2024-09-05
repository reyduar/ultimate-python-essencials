class Model:
    tabla = False
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que deifinr una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla}")

    @classmethod
    def buscar_id(self, _id):
        print(f"Buscando en {self.tabla} con id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = 'usuarios'

 
usuario = Usuario()
usuario.guardar()

Usuario.buscar_id(1)