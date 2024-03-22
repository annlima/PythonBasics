tope=0
arregloNumeros = [5,9,8,2,1,6,3,4,7,0]
n=len(arregloNumeros)
print("Arreglo desordenado ", arregloNumeros)

while(tope<n):
    i=n-1
    while(i>tope):
        if(arregloNumeros[i-1]>arregloNumeros[i]):
            valorMenor=arregloNumeros[i]
            arregloNumeros[i]=arregloNumeros[i-1]
            arregloNumeros[i-1]=valorMenor
            #end if
        i=i-1
        #endwhile
    tope=tope+1
#endwhile

print("*****************************************************")
print("El arreglo ordenado es", arregloNumeros)
