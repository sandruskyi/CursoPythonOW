from EjemploCompletoAlumnoDNIPersonaNotas.DNI import DNI
from EjemploCompletoAlumnoDNIPersonaNotas.Alumno import Alumno

if __name__=='__main__':
    dni = DNI('12345678')
    a1 = Alumno(dni, "Sandra", 23)
    print(a1)
    a1.addNotas("Cono",10)
    a1.addNotas("Mo",2)
    print(a1)
    a1.modNotas("Mo",10)
    print(a1)

    a = int(123.3)
    print(2 in range(1,11,2))