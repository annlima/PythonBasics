inicio=0
arregloNumeros = [5,9,8,2,1,6,3,4,7,0]
print("Arreglo desordenado ", arregloNumeros)
n = len(arregloNumeros)

while(inicio<n-1):
    indiceDelMenor=inicio
    valorMenor=arregloNumeros[inicio]
    i=inicio+1
    while(i<n):
        if(arregloNumeros[i]<valorMenor):
            indiceDelMenor=i
            valorMenor=arregloNumeros[i]
            #end if
        i=i+1
        #end while 
    arregloNumeros[indiceDelMenor]=arregloNumeros[inicio]
    arregloNumeros[inicio]=valorMenor
    inicio=inicio+1
    #end while

print("Numeros ordenados", arregloNumeros)
