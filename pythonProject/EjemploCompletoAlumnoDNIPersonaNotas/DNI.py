class DNI():
    """Vamos a crear el constructor, que recibe el número de DNI y calcula automáticamente la letra.
    Vamos a crear el constructor, que recibe el número de DNI y calcula automáticamente la letra.
    Crearemos también los métodos seters y getters.
    Se debe definir el método __str__ para imprimir los objetos."""

    def __init__(self,dni):
        self.dni = dni

    def __calcularLetra(self): # Método oculto para no utilizarlo desde fuera
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.dni)%23]

    @property ## Getter dni
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self,dni):
        if len(dni) == 8 and dni.isdigit():
            self._dni = dni
            self._letra = self.__calcularLetra()
        else:
            raise ValueError("DNI incorrecto")

    @property ## Getter letra - NO EXISTE SETTER DE ESTE
    def letra(self):
        return self._letra

    def __str__(self):
        return "DNI: {0}-{1}".format(self.dni, self.letra)
"""
if __name__=='__main__':
    dni = DNI("12345678")
    print(dni)
"""
