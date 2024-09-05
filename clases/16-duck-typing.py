
class Usuario():
    def guardar(self):
        print("Guardando usuario en BBDD")

class Session():
    def guardar(self):
        print("Guardando en archivo de sesion")

# duck typing es cuando se llama a un metodo sin importar la clase que sea siempre y cuando tenga el metodo que se esta llamando en la clase padre o en la clase hija 
# si camina como pato y hace cuac como pato entonces es un pato
def guardar_objeto(objetos):

    for objeto in objetos:
         objeto.guardar()

usuario = Usuario()
sesion = Session()
guardar_objeto([usuario, sesion])