#! /usr/bin/env python

class Notas():
    """La clase Notas nos permite guardar una serie de notas por asignatura.
    Creamos el constructor, teniendo en cuenta que la estructura de datos que vamos a utilizar para guardar asignaturas y notas será un diccionario.
    Creamos métodos para gestionar las notas: addnotas, modnotas, delnotas.
    Creamos un método que nos devuelve la media de las notas guardadas.
    Se debe definir el método __str__ para imprimir las asignaturas y sus correspondientes notas."""

    def __init__(self):
        self._notas = {} # Será un diccionario

    @property # Getter de notas
    def notas(self):
        resultado =""
        for key, value in self._notas.items(): # Recorremos el diccionario
            resultado += key+":"+str(value)+"\n"
        return resultado

    def addNotas(self,asig,nota):
        self._notas[asig]=nota
    def modNotas(self,asig,nota):
        if(asig in self._notas.keys()):
            self._notas[asig]=nota
        else:
            raise ValueError("Asignatura incorrecta")

    def delNotas(self, asig):
        if(asig in self._notas.keys()):
            del self._notas[asig]
        else:
            raise ValueError("Asignatura incorrecta")
    def media(self):
        return sum(self._notas.values())/len(self._notas.values())

    def __str__(self):
        resultado = ""
        for key,value in self._notas.items():
            resultado += key + ":" + str(value) + "\n"
        return resultado
"""
if __name__=='__main__':
    n = Notas()
    print(n)
    n.addNotas("Hola",10)
    print(n)
"""

