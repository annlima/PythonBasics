##############################################################
# Función para la búsqueda secuencial
# ALUMNA: ANDREA LIMA BLANCA
############################################################

def sequentialSearch(arreglo, elemento_buscar):
    i= 0
    encontrado = False
    while i < len(arreglo) and not encontrado:
        if arreglo[i] == elemento_buscar:
            encontrado = True
        else:
            i = i+1
    return i


lista=[1, 2, 3, 4, 5, 6, 7, 8, 9]

x=int(input("Número en el arreglo: " ))
if x in lista:
    print("Está en el lugar ", sequentialSearch(lista, x))
else:
    print("Intenta con otro número, ese no está en la lista.")


