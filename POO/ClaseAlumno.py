class Alumno():
    contador = 0

    def __init__(self,nombre = ""):
        self.nombre = nombre
        self._secreto = "claveSecreta" # Oculta pero accesible con a1._secreto
        self.__secreto = "claveSecreta" # Oculta pero accesible con a1._Alumno.__secreto
        Alumno.contador+=1


if __name__=='__main__':
    a1 = Alumno('Pepe')
    print(a1.nombre)
    print(Alumno.contador)
    a2 = Alumno('Sandra')
    print(Alumno.contador)
    print(a2._secreto)
    print(a2.__secreto)