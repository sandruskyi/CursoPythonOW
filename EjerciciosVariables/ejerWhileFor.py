#!/usr/bin/env python
"""
#1. Pedir un número por teclado y mostrar la tabla de multiplicar
n = int(input("nº: "))
cont = 0;
while(cont<11):
    print("%s * %s = %s" % (n, cont, n*cont))
    cont+=1

#2. Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120
n = int(input("nº: "))
numero = 1
for num in range(1,n+1):
    numero *=num
print(numero)

#3. Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.
n = int(input("nº: "))
adiv = int(input("adivinaº: "))
while(n!=adiv):
    if(n>adiv):
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")
    adiv = int(input("adivinaº: "))
else:
    print("Adivinado")

#4. Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
for i in range(1,5):
    for j in range (0,10):
        print("%s * %s = %s" % (i,j,i*j))
"""
#5. Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
n = int(input("nº: "))
primo = True
for i in range(1,n):
    if(i!=n and i!=1 and n%i==0):
        primo = False
print("Primo" if primo==True else "No primo")



