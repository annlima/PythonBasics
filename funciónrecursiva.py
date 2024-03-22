def factorialrecursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorialrecursivo(n-1)

x=int(input("¿Qué factorial necesitas? "))
print("Su factorial es: ", factorialrecursivo(x))