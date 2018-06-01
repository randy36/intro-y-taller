import math
from clasefig import fig
def Rectangulo(fig):
    def __init__(self, x, y, alto, ancho):
        super() .__init__(x,y)
        self.__alto = alto
        self.__ancho = ancho

    def getAlto(self):
        return self.__alto

    def setAlto(self,alto):
        self.__alto == alto

    def getAncho(self):
        return self.__ancho

    def setAncho(self,alto):
        self.__ancho == ancho

    def CalcularArea(self):
        return self.__alto * self.__ancho
