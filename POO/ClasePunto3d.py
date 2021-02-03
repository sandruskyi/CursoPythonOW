from ClasePuntoGetSet import PuntoGetSet as punto

class Class3d(punto):
    def __init__(self,x=0, y=0, z=0):
        super().__init__(x,y) ## Referencia a la clase madre PuntoGetSet
        self.z = z

    @property ## Getter z
    def z(self):
        return self._z

    @z.setter ## Setter z
    def z(self,z):
        self._z = z

    def __str__(self):
        return super().__str__()+":"+str(self.z)

    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.z - otro.z
        return(dx*dx + dy*dy + dz*dz)**0.5

if __name__=='__main__':
    p2D = punto(3,4)
    print(p2D) ## Utiliza la función str de PuntoGetSet
    print(dir(p2D)) ## Me devuelve los métodos y atributos que tiene
    p3D = Class3d(p2D,5)
    print(dir(p3D))
    print(p3D) ## Utiliza la función str de Punto3D


