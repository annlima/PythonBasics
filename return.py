def numeroentero():
    while (True):
        print("Ingresa un valor entero:")
        n = input("n: ")
        if n.isdigit():
            n = int(n)
            return n
        else:
            print("n debe ser entero")

num=numeroentero()
print(num)