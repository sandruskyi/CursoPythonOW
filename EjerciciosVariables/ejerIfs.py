#!/usr/bin/env python

"""
# 1. Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.
a = int(input("Introduzca un nº:"))
b = int(input("Introduzca un nº:"))
if ((a+b)<0):
    print("neg")
elif(a+b)>0:
    print("pos")
else:
    print("0")

# 2. Escribe un programa que lea un número e indique si es par o impar.
a = int(input("Introduzca un nº:"))
print("par" if ( a%2 ==0) else "impar")

# 3. Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
a = int(input("Introduzca un n entre 1 y 12º:"))
while ( a<1 or a>12):
    a = int(input("Introduzca un n entre 1 y 12º:"))
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print("31 días")
elif mes==4 or mes==6 or mes==9 or mes==11 :
    print("30 días")
elif mes==2:
    print("28 o 29 días")
else:
    print("Mes incorrecto")


# 4. Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
user = input("Usuario: ")
con = input("Contra: ")
if (user=="pepe" and con=="asdasd"):
    print("Has entrado al sistema")
else:
    print("Error")

# 5. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
a = int(input("Introduzca un año:"))
if (a%4==0)and (a%100!=0) or (a%400==0):
    print("bisiesto")
else:
    print("no bisiesto")
"""
#6. Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.
a = input("caracter: ")
if (a>="A" and a<="Z"):
    print("Mayus")
else:
    print("Minus")


