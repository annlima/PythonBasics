# Andrea Lima Blanca
# 7 de octubre de 2021
# Sucesión de Fibonacci
#inicio algoritmo
print("Ingrese la cantidad de elementos de la serie")

n=int(input("n= "))
a=0
b=1
fibonacciPares= []

#Validar que n sea entero
#inicia while
while(n<=0):
    print("ERROR: Debe ser un entero mayor que 0")
    n=int(input("n= "))
    #termina while

i=0
#inicia while (repetir mientras i<=n)
while (i<=n):
    print("El número de la serie en la posición ", i, "es ", a)
    c = a + b
    a = b
    b = c
    i+=1
    #inicia if (Si a%2 == 0)
    if a%2==0: 
        fibonacciPares.append(a)
        #termina if (termina si)
    #termina while (termina repetir)

print("Los números de la serie Fibonacci Pares son", fibonacciPares)

#iniciafor (Repetir por cada elemento de Fibonacci_Pares)
for n in fibonacciPares:
    print ("------------", n, "--------------")
    #termina for (Termina Repetir)

#fin algoritmo
