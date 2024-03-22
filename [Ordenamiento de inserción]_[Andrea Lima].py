##############################################################
# Ordenamiento de inserción directa
# ALUMNA: ANDREA LIMA BLANCA
# FECHA: 22-Oct-2021
############################################################

def directInsertSort(arreglo_desordenado):
    n = len(arreglo_desordenado)
    inicio = 0
    numIteracionesInternas = 0
    numIteraciones1erWhile = 0
    while (inicio < n-1):
        indiceDelMenor = inicio
        valorMenor = arreglo_desordenado[inicio]
        i = inicio + 1
        while ( i < n ):
            if ( arreglo_desordenado[i] < valorMenor):
                indiceDelMenor = i
                valorMenor = arreglo_desordenado[i]
            i = i + 1
            numIteracionesInternas = numIteracionesInternas +1
        arreglo_desordenado[indiceDelMenor] = arreglo_desordenado[inicio]
        arreglo_desordenado[inicio]=valorMenor
        inicio = inicio + 1
        numIteraciones1erWhile = numIteraciones1erWhile +1
    print("Numero iteraciones internas", numIteracionesInternas)
    print("Numero iteraciones 1er while", numIteraciones1erWhile)

arreglo= [9, 4, 3, 2, 6, 7, 1, 5, 8, 110, 32, -8]
print("Este es el arreglo desordenado, ", arreglo)

directInsertSort(arreglo)
print("Este es el arreglo ordenado, ", arreglo)