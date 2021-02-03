
class Circulo():
    """ Esta clase detalla las características de un círculo"""
    def __init__(self,radio=0):
        self.set_radio(radio)

    def set_radio(self,radio):
        if(radio>=0):
            self._radio = radio
        else:
            raise ValueError("Radio debe ser positivo. Radio = 0")
            self._radio = 0

    def get_radio(self):
        print("Devolvemos el radio")
        return self._radio

if __name__=='__main__':
    circulo = Circulo(1)
    print(circulo.get_radio())
    circulo.set_radio(5)
    print(circulo.get_radio())
    print(circulo)

