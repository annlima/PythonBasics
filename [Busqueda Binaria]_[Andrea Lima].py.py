##############################################################
# Función para la búsqueda binaria
# ALUMNA: ANDREA LIMA BLANCA
############################################################

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarySearch(lista, elemento_buscar):
   low = 0
   high = len(lista)-1
   while low <= high:
      mid = int((low + high)/2)
      aux = lista[mid]
      if aux == elemento_buscar:
         return mid
      if aux > elemento_buscar:
         high = mid -1
      else:
         low = mid + 1
   return None

x=int(input("Número en el arreglo: " ))

if x in lista:
   print("El índice de ese número es: ", binarySearch(lista, x))
else:
   print("Ese número no está dentro del arreglo, inténtalo de nuevo.")