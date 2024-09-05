from abc import ABC, abstractmethod

class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_id(self, _id):
        print(f"Buscando en {self.tabla} con id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = 'usuarios'

    def guardar(self):
        print(f"Guardando {self.tabla}")

 
usuario = Usuario()
usuario.guardar()

Usuario.buscar_id(1)