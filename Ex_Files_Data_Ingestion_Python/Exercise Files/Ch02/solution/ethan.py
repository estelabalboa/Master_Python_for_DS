import numpy as np

matrix_aux = [[1,2,3],
              [4,5,6],
              [7,8,9]]

m = np.array(matrix_aux)
print(m)

matriz_zeros = np.zeros((3,5))

# print(matriz_zeros)

#print(m[1,1])
#print(m[:,2])
#print(m[0,:])
# print(m[0,:-2])

# Sumamos todos los elementos de la columna 3 (la columna empieza en cero, uno y dos )
print(np.sum(m[:,2]))

# Calculamos la media de todos los elementos de la columna
print(np.average((m[:,2])))

# Calculamos la media de la fila primera
print(np.average((m[0,:])))


for i in range(len(m[0])):
    summ=0
    for x in m:
        summ+=x[i]
    print(summ)

matrizvacia=[]
numfilas=3
numcolumnas=3#le indicas cuantas columas y filas quieres que tenga la matriz

for i in range (numfilas):
    matrizvacia.append([0]*numcolumnas)
    for j in range(numcolumnas):
        matrizvacia[i][j]=int(input("fabrica " + str(i+1)+" dia " +str(j+1)))
        # le indicas valor a valor de la fila y columna

print(matrizvacia)

for i in range(len(matrizvacia[0])):#SUMA LOS ELEMENTOS DE LA MATRIZ PARA CADA COLUMNA
    summ=0
    for x in matrizvacia:
        summ+=x[i]
    print(summ)
    print(summ/len(matrizvacia[0]))

print(matrizvacia[0][2])# ACCEDER A LA FILA 1 COLUMNA