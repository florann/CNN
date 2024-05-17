#import numpy to create matrix easily 
import numpy as np
import threading as th
import concurrent.futures as ThreadManager
import random as rand
import keyboard as kb
#importing function
from PythonFunction.func_pathFinding import *


#Globals
rMatrix = 20
matrix = createMatrix(rMatrix)

def randomObstacle(matrix):
    #Calcul the number of total cells 
    totalCell = rMatrix*rMatrix
    #Number of cell that will be converted as obstacle
    obstaclePourcentage = 0.2
    totalObstacle = round(totalCell * obstaclePourcentage)
    #Crawling the whole matrix
    placedObstacle = 0
    while placedObstacle <= totalObstacle:
        for row in matrix:
            for column in row:
                if placedObstacle >= totalObstacle:
                    return 1
                print(getRandNumber())
                if getRandNumber() == 0:
                    column = -1
                print(column)
                return 1
    

    print("----------------------")
    print(totalCell)
    print(matrix)
    print(totalObstacle)

#randomObstacle(matrix)

#New method of creating matrix with obstacles
obstacleMatrix = createMatrixObstacle(20)
print(obstacleMatrix)
#printCordinateInsideMatrix(matrix)
position_start_input = input("Enter a position to start : ")
position_end_input = input("Enter a position to reach : ")

position_start_input = position_start_input.split(",")
position_end_input = position_end_input.split(",")
position_start_input = [int(x) for x in position_start_input]
position_end_input = [int(x) for x in position_end_input]
print(position_start_input)
print(position_end_input)


injectObstacleFromNumpyMatrix(matrix, obstacleMatrix)
print(matrix)
resultNode = pathfindingAStar(position_start_input, position_end_input, matrix)
print(printPath(resultNode))

#with ThreadManager.ThreadPoolExecutor() as executor:
#    #Starting threads with a pathfinding calculation
#    returnValue1 = executor.submit(pathfindingAStar, matrix[8][0],matrix[8][19])
#   returnValue2 = executor.submit(pathfindingAStar, matrix[0][8],matrix[19][8])

#   print(printPath(returnValue1.result()))
#   print(printPath(returnValue2.result()))


