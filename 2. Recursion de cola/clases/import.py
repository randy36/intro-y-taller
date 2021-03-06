import math
from clasefig import fig
class Circulo(fig):
    def __init__ (self ,x , y, r):
        super().__init__(x,y)
        self.__radio = r

    def getRadio(self):
        return self.__radio

    def setRadio(self,r):
        self.__radio=r

    def calcularArea(self):
        return math.pi * (self.__radio**2)
