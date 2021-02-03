class Clase():
    at_clase = 1
    def metodo(self):
        self.at_objeto = 2


objeto = Clase()
#print(objeto.at_objeto)
objeto.metodo()
print(objeto.at_objeto)
print(Clase.at_clase)