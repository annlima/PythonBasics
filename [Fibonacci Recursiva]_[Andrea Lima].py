# Práctica 8: Fibonacci recursiva
# Nombre del alumno: Andrea Lima Blanca 
# Fecha: 29 de octubre de 2021



def seriefibonacci_recursivo(lugar):
    if lugar==1 or lugar==0:
        return 1
    else:
        return seriefibonacci_recursivo(lugar - 1) + seriefibonacci_recursivo(lugar - 2)

x=int(input("¿Qué número en la serie necesitas? "))
print("El número en la serie de Fibonacci es: ", seriefibonacci_recursivo(x))