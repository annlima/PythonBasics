##################################################################
#  Ejercicio 4: Dar opción de volver a usar la calculadora
#  Alumna: Andrea Lima Blanca
#  Fecha: 24-Sep-2021
##################################################################

evalAgain = True
while evalAgain:
     print(" *************************************************** ")
     print("Ingrese dos valores, mayores que 0")

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

     print("¿DESEAS HACER OTRA OPERACIÓN?")     
     print("Respuesta válida: SI")
     respUser = input("Ingrese respuesta: ")
     if not((respUser == "si") or (respUser == "SI") or (respUser == "Si")):
         evalAgain = False
print("GRACIAS POR USAR ESTA CALCULADORA")     