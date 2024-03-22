# Práctica 6 // Programa 1
# Frecuencia de aparición de los números en una matriz
# Andrea Lima Blanca
# 15 de octubre de 2021

#VARIABLES 
i=0
n=0
j=0
frecuencias=[0,0,0,0,0]
import random

#INICIO
#MOSTRAR LONGITUD DE MATRIZ 
print("Ingrese la longitud de la matriz")
n=int(input("LONGITUD: "))

arreglo=[0]*n
matriz=[arreglo]*n

#INICIO FOR (PARA i 0 A i<n)
for i in range (n):
    #INICIO FOR (j 0 A j<n)
    for j in range(n):
        matriz[i][j]=random.randint(1,5)
    #FIN FOR
#FIN FOR

#MOSTRAR NÚMEROS
print(matriz)

#INICIA FOR 
for i in range (n):
    #INICIA FOR
    for j in range (n):
        #INICIA IF
        if matriz[i][j]==1:
            frecuencias[0]=frecuencias[0]+1
            #TERMINA IF
        #INICIA ELIF
        elif matriz[i][j]==2:
            frecuencias[1]=frecuencias[1]+1
            #TERMINA ELIF
        #INICIA ELIF
        elif matriz[i][j]==3:
            frecuencias[2]=frecuencias[2]+1
            #TERMINA ELIF
        #INICIA ELIF
        elif matriz[i][j]==4:
            frecuencias[3]=frecuencias[3]+1
            #TERMINA ELIF
        #INICIA ELSE
        else:
            frecuencias[4]=frecuencias[4]+1
            #TERMINA ELSE
    #TERMINA FOR 
 #TERMINA FOR

for i in range (5):
    print("El número de ", i+1, "'s, es", frecuencias[i])

#FIN