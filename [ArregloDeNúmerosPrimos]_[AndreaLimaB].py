# Práctica 5.2: Arreglo de números primos
# Nombre del alumno: Andrea Lima Blanca 
# Fecha:  2 de octubre de 2021

evalAgain=True 
while evalAgain:
    print("****************Números primos**************")
    numero= int(input("Número máximo...: "))
    n=0
    numeros = []
    if numero== 0:
        print("No puede ser 0")
        evalAgain=True
        
    for i in range (1, numero+1):
        for x in range (1, i+1):
            primo= True
            res=i%x
            if res==0 and x!=1 and x!=i:
                primo= False
                break
        if primo == True:
         n+=1
         numeros.append(i)
    
    print("El arreglo de números primos, sería: ", numeros)
    print("Número TOTAL de primos", n)
    
    print("¿Quieres intentarlo de nuevo? Respuesta válida: SI")
    respUser = input("Ingrese respuesta: ")
    if not((respUser == "si") or (respUser == "SI") or (respUser == "Si")):
        evalAgain = False

print("GRACIAS POR USAR NÚMEROS PRIMOS") 
    