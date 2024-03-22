#  Práctica3: Calculadora
#  Alumna: Andrea Lima Blanca
#  Fecha: 06-Sep-2021
#1.Solicite y reciba dos números enteros.
#2.Solicite y reciba la operación que se desea realizar: Suma (+), Resta (-) o división (/).
#3.Realice la operación solicitada con los dos números enteros.

A = int(input("A: "))
B = int(input("B: "))

suma= A+B 
resta= A-B, B-A
división= A/B, B/A

operacion= input("Inserte si quiere: sumar, restar o dividir: ")
if(operacion== "sumar"):
    print("El resultado de la suma de ", A, "y ", B," es igual a: ", suma)
elif(operacion== "restar"):
    print("El resultado de la suma de ", A, "-", B,"y", B,"-", A,"es igual a: ", resta)
elif(operacion== "dividir"):
    print("El resultado de la suma de ", A, "/", B,"y", B,"/", A,"es igual a: ", división)