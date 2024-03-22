# Práctica 5.1: Arreglo de números 
# Nombre del alumno: Andrea Lima Blanca 
# Fecha: 2 de octubre de 2021

print("*************ARREGLOS**************")
print("Ingresa el tamaño de tu arreglo")
n = int(input("n = "))
numeros = []
i = 0
suma=0
while i < n:
    print("Ingresa el número ", i+1)
    numero = input("número = ")

    if (numero.isdigit()):
        numero = int(numero)
        i+=1
        numeros.append(numero)
    else:
        print("ERROR: Ingrese un número entero. ")
    
print("Arreglo número = ", numeros)

print("***************** S U M A ********************")
for valor in numeros:
    suma = suma + valor

print("La suma es", suma)

print("************** P R O M E D I O ***************")
promedio = suma/n
print("El promedio es", promedio)

print("************** M Á X  Y  M I N ***************")
max = 0
min = numeros[0]
for number in numeros:
    print("Valor de number ", number)
    if (number > max ):
        max= number
    if (number < min ):
        min = number

print ("El número máximo del arreglo es ", max)

print ("El número minimo del arreglo es ", min)

