class Calculadora():
    """ Tiene métodos estáticos """

    def __init__(self,nombre):
        self.nombre = nombre

    def modelo(self):
        return self.nombre

    @staticmethod
    def sumar(x,y): # Método estático que no depende de ningún parámetro de la clase
        return x+y

if __name__ == '__main__':
    c1=Calculadora("basica")
    print(c1.modelo())
    print(c1.sumar(5,5))

    print(getattr(c1,"nombre"))
    setattr(c1,"nombre","compleja")
    print(getattr(c1, "nombre"))
    print(hasattr(c1,"nombre"))