# Práctica 6 // Programa 2
# Frecuencia de aparición de los números pares e impares
# Andrea Lima Blanca
# 15 de octubre de 2021

#VARIABLES 
i=0
n=0
j=0
import random

#LONGITUD DE MATRIZ
print("Ingrese la longitud de la matriz")
#INGRESO DE LONGITUD
n=int(input("LONGITUD: "))

#VARIABLES
arreglo=[0]*n
matriz=[arreglo]*n

#INICIA FOR (NÚMEROS ALEATORIOS)
for i in range (n):
    #INICIA FOR
    for j in range(n):
        #MATRIZ NÚMEROS ALEATORIOS 1-100
        matriz[i][j]=random.randint(1,100)
        #FIN FOR 
    #FIN FOR

#SE IMPRIMEN LOS NÚMEROS
print(matriz)

#VARIABLES
a=0
b=0

#SE INICIA FOR (SABER SI ES PAR O IMPAR)
for i in range (n):
    #SE INICIA FOR
    for j in range (n):
        #SE INICIA SI (EVALUAR PAR)
        if (matriz[i][j] % 2 == 0):
            #SE AGREGA A LOS PARES
            a+=1
            #TERMINA SI
        #EMPIEZA ELSE
        else: 
            #SE AGREGA A LOS IMPARES
            b+=1
            #TERMINA ELSE

#SE IMPRIMEN LA CANTIDAD DE P E I QUE HAY
print("Los números pares que hay en la matriz son: ", a)
print("Los números impares que hay en la matriz son: ", b)

