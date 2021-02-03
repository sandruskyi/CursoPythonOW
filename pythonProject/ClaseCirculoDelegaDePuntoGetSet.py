from ClasePuntoGetSet import PuntoGetSet as Punto

class Circulo():

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    @property
    def centro(self):
        return self._centro

    @centro.setter
    def centro(self, nuevoCen):
        self._centro = nuevoCen

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, nuevoRad):
        self._radio = nuevoRad

    def __str__(self):
        return "Centro:{0}. Radio:{1}".format(self.centro.__str__(), self.radio)

if __name__=='__main__':
    p1 = Punto(2,3)
    print(p1)
    c1 = Circulo(p1,10)
    print(c1)
    p1.x = 5
    p1.y = 6
    print(p1)
    print(c1)
    c1.centro = p1
    print(c1)
    print(c1.centro)