#import numpy to create matrix easily 
import numpy as np

from function.fun_matrix import *

#Creating matrix
matrix = []

#Max matrice range
rMatrix = 4

#Creation of the matrix
matrix = createMatrix(rMatrix)

#Start coordinated
cStart = matrix[1][1]
#End coordinated
cEnd = matrix[3][3]

#Calculation of the matrix cost
costMatrix = calculateCost(matrix,rMatrix)
#Calculation of the Manhattan distance
manhattanMatrix = calculateManhattanDistance(matrix, rMatrix, cEnd)
#Computation to find f(n)
computedMatrix = addMatrixCostManhattan(costMatrix, manhattanMatrix, rMatrix)
#Path finding

print(matrix[0][-1])
print(matrix)
print(computedMatrix)
pathfindingMatrix4direction(matrix, computedMatrix, rMatrix, cEnd)
