#! usr/bin/env python

#1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
"""nombre = input("Dime tu nombre ")
print("Hola %s" % nombre)

#2. Calcular el perímetro y área de un rectángulo dada su base y su altura. Calcular también el perímetro y área de un triangulo.
print("Rectángulo")
base = float(input("Dime la base \n"))
altura = float(input("Dime la Altura \n"))
perimetro = 2*base + 2*altura
area = base * altura
print("Resultado Rectángulo: Area=%.2f Perimetro=%.2f" % (area,perimetro))

print("Triángulo")
baseT = float(input("Dime la base \n"))
ladoA = float(input("Dime un lado a"))
ladoB = float(input("Dime un lado b"))
alturaT = float(input("Dime la Altura \n"))
perimetroT = baseT + ladoA + ladoB
areaT = (baseT*alturaT)/2
print("Resultado Triángulo: Area=%.2f Perimetro=%.2f" % (areaT,perimetroT))


# 4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
num1 = float(input("Introduce un número: \n"))
num2 = float(input("Introduce otro número: \n"))
suma = num1 + num2
resta = num1 - num2
mult = num1*num2
div = num1/num2
resto = num1%num2
print("sum %.2f resta %.2f mult %.2f div %.2f resto %.2f " % (suma, resta, mult, div, resto))

# O :
num1=float(input("Numero1:"))
num2=float(input("Numero2:"))
print ("Suma:%d,resta:%d,multiplicacion:%d,division:%.2f"%(num1+num2,num1-num2,num1*num2,num1/num2))


# 5. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, con espacios intermedios.
palabra = input("Introduzca una palabra: ")
print((palabra+" ")*1000)


# 6. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minutos = int(input("Minutos: "))
horas = minutos / 60
minutos = minutos % 60
print("%s horas y %s segundos " % (int(horas),minutos))

# OTROS:
print(all([True, True, True]))
print(all([True, True, False]))
print(all([]))
print(any([True, True, True]))
print(any([True, True, False]))
print(any([]))
"""

lng = "es"
print("HOLA" if lng=="es" else "HI")