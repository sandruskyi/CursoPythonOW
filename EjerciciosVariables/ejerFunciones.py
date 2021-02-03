#!/usr/bin/env python
"""
#1. Escribir dos funciones que permitan calcular:
# -La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# -La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
def cantSeg(horas, min, seg):
    return horas*60*60 + min*60 +seg
def cantHMS(seg):
    horas = seg / 3600
    seg -= horas * 3600
    minutos = seg%3600
    seg -=minutos*60
    return horas, minutos, seg
print(cantSeg(5,6,20))
print(cantHMS(18380))

#2. Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:
#Si recibe un argumento, supone que son segundos y convierte a horas, mintos y segundos.
#Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.
def calcular(*args):
    if len(args)==1:
        return cantHMS(args[0])
    elif len(args)==3:
        return cantSeg(*args)
    else:
        raise TypeError("TypeError se esperaban más parámetros")
print(calcular(1,2,3))

# 3. Queremos hacer una función que añada a una lista los contactos de una agenda. Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre, el campo del teléfono, aunque puede tener más campos. Los datos se irán pidiendo por teclado, se pedirá de antemanos cuantos contactos se van a guardar. Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el “*”.
def guardar_agenda(l_agenda, **kwargs):
    l_agenda.append(kwargs)
    return l_agenda
def main():
    agenda = []
    cantidad = int(input("¿Cuantos contactos introducirá?"))
    for i in range(cantidad):
        contacto = {}
        contacto["nombre"] = input("Nombre: ")
        contacto["telefono"]= input("Telefono: ")
        campo = input("¿Desea más campos? Introduzcalo o pulse * en caso contrario")
        while campo != '*':
            contacto[campo] = input("Valor del nuevo campo")
            campo = input("¿Desea más campos? Introduzcalo o pulse * en caso contrario")
        agenda = guardar_agenda(agenda, **contacto)
    print(agenda)
if __name__=='__main__':
    main()
"""
#5. Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista:
def multiplicar(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista.pop()*multiplicar(lista)

if __name__ == '__main__':
    print(multiplicar([3,4,5]))





