n1 = int(input("Ingresa un valor: "))
n2 = int(input("Ingresa un valor: "))

def numero1 (numentero): 
    if (numentero > 0): 
        sum1 = 0 
        limite = numentero // 2 
        num = 1
        for i in range (limite + 1): 
            if (numentero % num == 0): 
                sum1 = sum1 + num
            num+=1
    return sum1

def numero2 (numentero): 
    if (numentero > 0): 
        sum2 = 0 
        limite = numentero // 2 
        num = 1
        for i in range (limite + 1): 
            if (numentero % num == 0): 
                sum2 = sum2 + num
            num+=1
    return sum2

num1 = numero1(n1)
num2 = numero2(n2)

if (num1 == n2) and (num2 == n1): 
    print ( "Número", n1 ,"es amigo de", n2)
else: 
    print ( "Número", n1 ,"no es amigo de", n2)