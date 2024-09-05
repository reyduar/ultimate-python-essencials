from abc import ABC, abstractmethod

class Model(ABC):
        @abstractmethod
        def guardar(self):
            pass

class Usuario(Model):
    def guardar(self):
        print("Guardando usuario en BBDD")

class Session(Model):
    def guardar(self):
        print("Guardando en archivo de sesion")


def guardar_objeto(objetos):
    for objeto in objetos:
         objeto.guardar()

usuario = Usuario()
sesion = Session()
guardar_objeto([usuario, sesion])