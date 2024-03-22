matriz1= [[8, 9, 7], [6, 9, 2], [8, 5, 9]]
matriz2= [[6, 8, 6], [8, 9, 5], [8, 9, 7]]
sumaM=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numeroRenglones= 3
columnas= 3

for i in range(0, numeroRenglones, 1):
    for j in range (0, columnas, 1):
        sumaM[i][j]= matriz1[i][j]+ matriz2[i][j]

print ("SUMA", sumaM)

matriz1= [[8, 9, 7], [6, 9, 2], [8, 5, 9]]
matriz2= [[6, 8, 6], [8, 9, 5], [8, 9, 7]]
i=0
j=0
k=0
mulMat=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range (0, numeroRenglones, 1):
    for j in range (0, columnas, 1):
        for k in range (0, columnas, 1):
            mulMat[i][j]= mulMat[i][j]+matriz1[i][k]*matriz2[k][j]

print("MULTPLICACIÓN", mulMat)