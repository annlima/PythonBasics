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
n = int(input("Ingrese el elemento de 0 - 10: "))

# Búsqueda secuencial
encontrado= False
i=0 
x=len(arregloNumeros)

while (i< x) & (not encontrado):
    if n== arregloNumeros[i]:
        encontrado =True
        break 
    i=i+1
    break 
    #end if
#end for


if (encontrado== False):
    print("El elemento ", n, " no se encontró.")
else:
    print("El elemento ", n, "se encontró")


