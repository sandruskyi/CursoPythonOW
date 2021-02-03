class Gato():
    def hablar(self):
        print("Miau")

class Perro():
    def hablar(self):
        print("Guau")

def escucharMascota(animal):
    animal.hablar()

if __name__=='__main__':
    g = Gato()
    p = Perro()
    escucharMascota(g)
    escucharMascota(p)
