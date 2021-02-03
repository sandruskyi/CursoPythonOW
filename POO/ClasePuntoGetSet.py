import math

class PuntoGetSet():
    """ Representación de un punto en el plano, los atributos son x e y
    que representan los valores de las coordenadas cartesianas."""

    def __init__(self,x=0, y=0): # Constructor
        self.x = x
        self.y = y

    @property ## Getter x
    def x(self):
        return self._x

    @x.setter ## Setter x
    def x(self,x):
        self._x = x

    @property ## Getter y
    def y(self):
        return self._y

    @y.setter ## Setter y
    def y(self,y):
        self._y = y

    def __str__(self):
        return "{0}:{1}".format(self.x,self.y)

    def distancia(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx*dx + dy*dy)**0.5
"""
if __name__ == '__main__':
    punto1 = PuntoGetSet()
    punto2 = PuntoGetSet(4,5)
    print(punto1.x, punto1.y , punto2.x, punto2.y)
    print(punto1.distancia(punto2))
    print(punto1)
    punto1.x= 5
    print(punto1)"""