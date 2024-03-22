#Nombre del alumno: Andrea Lima Blanca
#Fecha: 4 de noviembre de 2021
#Programa de 3er examen parcial: Números amigos

#Inicia programa
#Inicia función sumaDivisores(número entero)
def sumaDivisores(numeroEntero):
    #inicia If
    if numeroEntero > 0:
        suma=0
        limite=numeroEntero//2
        #inicia for
        num=1
        for i in range(limite+1):
            #inicia if 
            if numeroEntero%num==0:
                suma=suma+num
                #termina if
            num+=1
            #termina for 
        return suma
        #termina if 
    #termina función sumaDivisores

numero1= int(input("Elige un número entero: "))
numero2= int(input("Elige otro número entero: "))


#inicia if
if (sumaDivisores(numero1)==numero2) and (sumaDivisores(numero2)==numero1):
    print("El número ", numero1, "es amigo de ", numero2)
#inicia else
else:
    print("El número ", numero1, "no es amigo del ", numero2)
#termina if y else

#termina el programa
