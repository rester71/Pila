
class Pila(object):

    __tam = None
    __tope = None
    __datos = None

    def __init__(self, tam):
        self.__tam = tam
        self.__datos = []

    def push(self, dato):
        if self.llena():
            return False
        else:
            self.__datos.append(dato)
            return True

    def llena(self):
        if len(self.__datos) == self.__tam:
            return True
        else:
            return False

    def pop(self):
        if self.vacia():
            return True
        else:
            valor = self.__datos.pop()
            return valor

    def vacia(self):
        if len(self.__datos) == 0:
            return True
        else:
            return False
