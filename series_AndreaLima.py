##################################################################
#  Ejercicio 4: Series
#  Alumna: Andrea Lima Blanca
#  Fecha: 24-Sep-2021
# Instrucciones: Realizar un programa para imprimir la serie: 1, 5, 8 12, 15, 19, 22, 26, 29, … n, así como la suma final de los números. 
# El programa deberá solicitar la usuario el límite máximo a calcular, número entero mayor a 0.
##################################################################





evalAgain = True
while evalAgain:
    print("¿Qué número deseas calcular?")
    print("RECUERDA: Debe ser mayor que 0")

    numero=int(input("Máximo a calcular: "))
   
    if not(numero>0):
        print("Recuerda que debe ser mayor que 0")
        evalAgain= True
    else:
        z= 1
        x= 1
        y= 1
        sumaTotal = 0

        while (z<=numero):
         print(z)
         sumaTotal = sumaTotal + z
         if (x== 1):
             z = z + 4
             x += 1
         else:
             z = z + 3
             x -=1
        print("La suma total es:",sumaTotal)
    print("Puedes realizar otra serie, respuesta válida: SI")
    respUser=(input("¿Quieres realizar otra serie?:   "))
    if not ((respUser == "si") or (respUser == "SI") or (respUser == "Si")):
        evalAgain=False

print("Gracias por usar Series")


    


    

        