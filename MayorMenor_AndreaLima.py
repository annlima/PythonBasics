#  Practica3: Mayor y Menor
#  Alumna: Andrea Lima Blanca
#  Fecha: 06-Sep-2021
# Algoritmo en un diagrama de flujo y programa en Python que solicite tres números enteros, los compare y retorne cuál de ellos es el menor y cuál es el mayor.

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if (A>B)&(B>C):
    print("A= ", A, " es mayor")
    print("B= ", B, " es menor," " C= ", C, " es menor")
if(B>A)&(A>C):
    print("B= ", B, " es mayor")
    print("A= ", A, "es menor," " C= ", C, "es menor")
if(C>A)&(A>B):
    print("C= ", C, " es mayor")
    print("A= ", A, "es menor," " B= ", B, "es menor")

print("FIN")
