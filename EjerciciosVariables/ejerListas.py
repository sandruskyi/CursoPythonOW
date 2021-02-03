#!/usr/bin/env python

"""
#1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. Muestra el máximo de los números guardado en la lista, muestra los números pares.
num=0
lista = []
while num>=0:
    num = int(input("nº: "))
    if(num>=0):
        lista.append(num)

lista.sort()
print(max(lista))
print(lista[len(lista)-1])
for i in range(len(lista)):
    if(lista[i]%2==0):
        print(lista[i])

#2. Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
lista=['Di', 'buen', 'dia', 'a', 'papa']
print(lista[::-1])

#3. Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista, y por último borra la cadena de la lista
lista=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]
cadena=input("Cadena:")
count= 0
if cadena in lista:
    for i in range(len(lista)):
        if lista[i]==cadena:
            count +=1
    print("Está %s veces" % (count))
else:
    print("No está")
cadena=input("Cadena2:")
print(lista)
lista[1]=cadena
print(lista)
del(lista[1])
print(lista)
"""
#4. Dado una lista, hacer un programa que indique si está ordenada o no.
lista=[2,3,4,1]
lista2=lista[:]
lista2.sort()
ordenada = True
for i in range(len(lista2)):
    if lista2[i]!=lista[i]:
        ordenada = False
if(ordenada):
    print("ordenada")
else:
    print("No")




