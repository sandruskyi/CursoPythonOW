class Telefono():
    "Clase telefono"
    def __init__(self,numero):
        self.numero = numero

    @property ## Getter numero
    def numero(self):
        return self._numero

    @numero.setter # Setter numero
    def numero(self, nuevoNum):
        self._numero = nuevoNum

    def telefonear(self):
        print("Llamando")

    def colgar(self):
        print("Colgando")

    def __str__(self):
        return self.numero

class Camara():
    "Clase camara"
    def __init__(self,mpx):
        self.mpx = mpx

    @property  ## Getter mpx
    def mpx(self):
        return self._mpx

    @mpx.setter  # Setter mpx
    def mpx(self, nuevoMpx):
        self._mpx = nuevoMpx

    def fotografiar(self):
        print('fotografiando')

    def __str__(self):
        return self.mpx

class Reproductor():
    "Clase Reproductor Mp3"
    def __init__(self,capacidad):
        self.capacidad=capacidad

    @property  ## Getter capacidad
    def capacidad(self):
        return self._capacidad

    @capacidad.setter  # Setter mpx
    def capacidad(self, nuevoCapa):
        self._capacidad = nuevoCapa

    def reproducirmp3(self):
        print('reproduciendo mp3')

    def reproducirvideo(self):
        print('reproduciendo video')

    def __str__(self):
        return self.capacidad

class Movil(Telefono,Camara,Reproductor):
    def __init__(self,numero,mpx,capacidad):
        Telefono.__init__(self,numero)
        Camara.__init__(self,mpx)
        Reproductor.__init__(self,capacidad)

    def __str__(self):
        return "Número: {0}, Cámara: {1}, Reproductor: {2}".\
            format(Telefono.__str__(self),Camara.__str__(self), Reproductor.__str__(self))

if __name__=='__main__':
    miMovil = Movil("234567843", "24", "125")
    print(miMovil)
    print(issubclass(Movil,Telefono))
    print(issubclass( Telefono, Movil ))
    print(isinstance(Movil, Telefono))
    print(isinstance(miMovil, Movil))
    print(isinstance(miMovil, Telefono))

