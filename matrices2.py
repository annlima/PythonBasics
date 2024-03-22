matriz1= [[1, 2], [3, 4], [5, 6]]
matriz2= [[1, 2, 3], [3, 4, 5]]

mulMat=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

renglonesm1=3
columnasm1=2
renglonesm2=2
columnasm2=3

i=0
j=0
k=0

for i in range (0, renglonesm1, 1):
    for j in range (0, columnasm2, 1):
        for k in range (0, columnasm1, 1):
            mulMat[i][j]= mulMat[i][j]+matriz1[i][k]*matriz2[k][j]

print("MULTPLICACIÓN", mulMat)