##################################################################################
# EJERCICIO: Búsqueda secuencial 
# Profesora: Karen Santiago
# Fecha: 14 Octubre 2021
##################################################################################

#Importar librería random
import random

#Arreglo de 10 ceros
arregloNumeros = [0]*10

#Llenar el arreglo con números aleagorios de 1 - 5
for i in range(len(arregloNumeros)):
    arregloNumeros[i] = random.randint(1,5)
#end for

print(arregloNumeros)

#algoritmo de búsqueda secuencial 
elemento = int(input("Ingrese el elemento de 0 - 10: "))

# Búsqueda secuencial
indice=[]
for i in range(len(arregloNumeros)):
    if (elemento == arregloNumeros[i]):
        indice.append(i)
    #end if
#end for


if (indice== []):
    print("El elemento ", elemento, " no se encontró.")
else:
    print("El elemento ", elemento, " se encontró en la posición: ", indice)



