
class Circulo():
    """ Esta clase detalla las características de un círculo"""
    def __init__(self,radio=0):
        self.radio= radio ## Para el setter

    @property
    def radio(self):  # Getter
        print("Devolvemos el radio")
        return self._radio

    @radio.setter
    def radio(self,radio):
        if(radio>=0):
            self._radio = radio
        else:
            raise ValueError("Radio debe ser positivo. Radio = 0")
            self._radio = 0

    @radio.deleter
    def radio(self):
        del self._radio

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase,self.radio)

    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})"
        return msg.format(clase, self.radio)

    def __eq__(self,otro):
        return self.radio == otro.radio

    def __add__(self, otro):
        self.radio+=otro.radio

    def __sub__(self, otro):
        if self.radio-otro.radio>=0:
            self.radio-=otro.radio
        else:
            raise ValueError("No se pueden restar")



if __name__=='__main__':
    circulo = Circulo(1)
    print(circulo.radio)
    circulo.radio = 5
    print(circulo.radio)
    print(circulo) ## Método __str__
    print(repr(circulo)) ## Método __repr__
    c2 = Circulo(3)
    print(circulo==c2) ## Método __eq__
    print(circulo.radio)
    print(c2.radio)
    circulo + c2
    print(circulo.radio)
    print(c2.radio)
    circulo - c2
    print(circulo.radio)

