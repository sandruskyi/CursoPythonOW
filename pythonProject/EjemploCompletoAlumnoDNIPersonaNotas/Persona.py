#! /usr/bin/env python
#from EjemploCompletoAlumnoDNIPersonaNotas.DNI import DNI

class Persona():
    """A continuación creamos la clase Persona. Una persona tendrá un DNI, un nombre y una edad.
    Creamos el constructor.
    Crearemos también los métodos seters y getters.
    Se debe definir el método __str__ para imprimir los objetos."""

    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    @property
    def dni(self):
        return self._dni
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @dni.setter
    def dni(self,dni):
        self._dni = dni
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @edad.setter
    def edad(self,edad):
        if edad>0:
            self._edad = edad
        else:
            raise ValueError("Edad incorrecta")

    def __str__(self):
        return self.dni.__str__() + " " +self.nombre + " " + str(self.edad)
"""
if __name__=='__main__':
    dni = DNI("12345678")
    p = Persona(dni, 'Sandra', 23)
    print(p)
"""


