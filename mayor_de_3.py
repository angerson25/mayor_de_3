#Programa: mayor de tres numeros

import math
print("----------")
print("---MAYOR-DE-3-NUMEROS--")

#input
a=int(input("Digite el valor de a"))
b=int(input("Digite el valor de b"))
c=int(input("Digite el valor de c"))
mayor= ""
#procesamiento
if a > b:
    if a > c:
        mayor = a
    else: 
        mayor = c
else:
    if b > c:
        mayor = b
    else:
        mayor = c

#output
print("---RESULTADOS---")
print("El mayor entre " + str(a) + " , " + str(b) + " y " + str(c) + " es: " + str(mayor))