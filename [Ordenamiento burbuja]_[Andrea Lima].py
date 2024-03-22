##############################################################
# Función para ordenar por burbuja
# ALUMNA: ANDREA LIMA BLANCA
# FECHA: 22-Oct-2021
############################################################

def bubbleSort(arreglo_desordenado):
    n = len(arreglo_desordenado)
    tope = 0
    numIteracionesInternas = 0
    while tope < n :
        i = n-1
        while ( i > tope):
            if (arreglo_desordenado[i-1] > arreglo_desordenado[i]):
                valorMenor = arreglo_desordenado[i]
                arreglo_desordenado[i] = arreglo_desordenado[i-1]
                arreglo_desordenado[i-1] = valorMenor
            i = i-1
            numIteracionesInternas = numIteracionesInternas + 1
        tope=tope+1

arreglo= [9, 4, 3, 2, 6, 7, 1, 5, 8, 110, 32, -8]
print("Este es el arreglo desordenado, ", arreglo)

bubbleSort(arreglo)
print("Este es el arreglo ordenado, ", arreglo)