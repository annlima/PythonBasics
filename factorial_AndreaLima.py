##################################################################
#  Ejercicio 4: Factorial
#  Alumna: Andrea Lima Blanca
#  Fecha: 24-Sep-2021
##################################################################

evalAgain= True
while evalAgain:
    print("FACTORIALES")
    print("ELIJA UN VALOR ENTERO")

    x = int(input("Ingrese el valor: "))
    factorial= 1
    uno=1
    q=x
    print("¿Cuál iteración quieres usar: for o while?")
    iteracion=(input("Ingrese la iteración: "))

    if(x==0):
        print("El factorial de 0 es 1")
    else:
        if (iteracion == "for"):
            for a in range(x):
                factorial= factorial * q
                q  = q - 1
                uno = x * q
                if (x > 0):
                    print (x,"*",q,"=", uno)
            print("El factorial de",x,"calculado con for es:", factorial)
        else:
            while(True):
                factorial = factorial * q
                q= q - 1
                uno= x * q
                if (q > 0):
                    print (x,"*",q,"=", uno)
                else:
                    break     
            print("El factorial de",x ,"calculado con while es:",factorial)
    print("¿Desea calcular otro factorial?")
    print("Respuesta válida: SI")
    respUser= input("Ingrese respuesta: ")
    if not(respUser=="SI"):
        evalAgain= False
print("Gracias por usar factoriales")
