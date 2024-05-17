import copy
import numpy as np
import random as rand
from dataclasses import dataclass

#BASIC FUNCTION FOR MATRIX 
#function to build a matrix with a specific size
def createMatrix(rMatrix):
    modCount = -1
    matrix = []
    bRow = [] 
    for x in range(rMatrix*rMatrix):
        #It mean a row need to be create
        #Each modulo 4
        if x%rMatrix == 0:   
            if modCount >= 0:
                #We add the row to the matrix
                matrix.append(bRow)
                bRow = [] 
            modCount += 1
        #Building row
        bRow.append([modCount,x%rMatrix])
        #Retrieving the last row
        if ((rMatrix*rMatrix) - 1) == x:
            matrix.append(bRow)
    return matrix


#Function that will create obstacle inside a matrix. The default value of obstacle is -1
def createObstacle(listObstacle, matrix):
    for obstacle in listObstacle:
        Y = obstacle[0]
        X = obstacle[1]
        matrix[Y][X] = -1

def printCordinateInsideMatrix(p_matrix: np.matrix):
    cptRow = 0
    cptColumn = 0
    
    dummyMatrix = copy.deepcopy(p_matrix)

    for row in p_matrix:
        cptColumn = 0
        for column in row: 
            dummyMatrix[cptRow][cptColumn] = [cptRow, cptColumn]
            cptColumn = cptColumn + 1
    cptRow = cptRow + 1
    print(dummyMatrix)


#Function that will create obstacle inside a matrix in a procedural way
#Description of the procedure : 
# - We will tag each matrix cells respecting the specific pattern
# - The function will have 2 parameters, the matrix itself and a shift value
#    -> The shift value will be use to generate the obstacle with a specific distance between them. To resume it will be the 
# size of obstacles.
# - After tagging matrix cells, we will do another crawling in to create real obstacle dimension ( It's probaly better to do the whole
# job with only one itteration ) 
# Constrain : The matrix must be crawlable be the pathfinding function so we need to have 'road' that can be travel.
# Information : The formula to place properly obstacle is (Shift x 2) + 1
def createObstacleProcedural(matrix, shift):
    #Shift move
    shiftMove = (shift*2)+1 #Need to by dynamic
    #Cross movement 
    moves = [[shiftMove,0],[0,shiftMove],[-shiftMove,0],[0,-shiftMove]]
    numberOfLine = matrix.count()
    numberOfColumn = matrix[0].count()
    cptLine = 0
    cptColumn = 0
    #Crawl the matrix from the beginning + 1
    while cptLine <= numberOfLine:
        while cptColumn <= numberOfColumn:
            cptColumn += 1
        cptLine += 1
    #Other method without crawling all cells of the matrix
    obstacleToPlace = True
    positionLine = 0
    positionColumn = 1
    while obstacleToPlace == True:
        if matrix[positionLine][positionColumn] != -1:
            matrix[positionLine][positionColumn] = -1
        for move in moves:
            if (matrix[positionLine + move[0]][positionColumn + move[1]] != -1 
            and (positionLine + move[0] < numberOfLine) and (positionLine + move[0] > 0) 
            and (positionColumn + move[0] < numberOfColumn) and (positionColumn + move[0] > 0)) :
                matrix[positionLine + move[0]][positionColumn + move[1]] = -1
            
#Functon de get a radom number between 0 and the specify range
#p_maxValue : Multiply the float between 0 & 1 by this value
#p_value : The range that can be returned
def getRandNumber(p_multiplyCoef,p_value):
    return round(rand.random()*p_multiplyCoef)%p_value

def findFirstValueOccurenceLinear(p_matrix, p_value):
    for row in range(p_matrix.shape[0]) :
        for column in range(p_matrix.shape[0]) : 
            if(p_matrix[row, column] == p_value):
                return (row, column)
    return -1


def shuffleMatrixPosition(p_matrix):
    coordinates = []
    for row in range(p_matrix.shape[0]):
        for column in range(p_matrix.shape[1]):
            coordinates.append((row, column))

    rand.shuffle(coordinates)
    return coordinates

def findFirstValueOccurenceRandom(p_matrix, p_coordinates, p_value):
    for position in p_coordinates:
        if(p_matrix[position[0],position[1]] == p_value):
            return(position)
    return -1


#Different approach, we will use the slicing method of python to create square obstacles
def createMatrixObstacle(p_size):
    matrix = np.zeros((p_size,p_size), dtype=int)
    cpt = 2
    lstObstacle = []
    #Creation of obstacles
    while cpt < 5:
        tmpMatrixObstacle = np.zeros(((cpt+1),(cpt+1)), dtype=int)
        tmpMatrixObstacle[0, :] = -2
        tmpMatrixObstacle[:, 0] = -2
        tmpMatrixObstacle[-1, :] = -2
        tmpMatrixObstacle[:, -1] = -2
        tmpMatrixObstacle[tmpMatrixObstacle == 0] = -1
        lstObstacle.append(tmpMatrixObstacle) 
        cpt = cpt + 1
    
    print(lstObstacle)
    #Shuffle matrix postion store in a list 
    coordinates = shuffleMatrixPosition(matrix)
    #Adding obstacles to matrix
    while findFirstValueOccurenceRandom(matrix, coordinates, 0) != -1:
        #Crawling the shuffled matrix to get a coordinate
        position = findFirstValueOccurenceRandom(matrix, coordinates, 0)
        #Choosing randomly an obstacle size
        obstacleSize = getRandNumber(10,3) + 1
        tmpObstacle = lstObstacle[obstacleSize - 1]
        #Create a dummy matrix for comparison
        zeroObstacle = np.zeros((obstacleSize,obstacleSize), dtype=int)
        #Extracting an obstacle's size submatrix off the main matrix 
        subMatrix = matrix[position[0]:position[0]+obstacleSize, position[1]:position[1]+obstacleSize]
        # print("SubMatrix")
        # print(subMatrix)
        # print(obstacleSize)
        # print(position)
        #Check if any of the cell of the extracted matrix contain an obstacle
        isFit = False
        if subMatrix.shape == zeroObstacle.shape and np.all(subMatrix == zeroObstacle):
            isFit = True

        if not isFit:
            #One chance in 10 to create arbitrary an obstacle
            randNum = getRandNumber(10,8)
            if randNum == 0:
                matrix[position[0]:position[0]+tmpObstacle.shape[0], position[1]:position[1]+tmpObstacle.shape[1]] = -3
            else: 
                matrix[position[0]:position[0]+tmpObstacle.shape[0], position[1]:position[1]+tmpObstacle.shape[1]] = 0
        elif((position[0] + tmpObstacle.shape[0] <= matrix.shape[0]) and (position[1] + tmpObstacle.shape[1] <= matrix.shape[1])):
            matrix[position[0]:position[0]+tmpObstacle.shape[0], position[1]:position[1]+tmpObstacle.shape[1]] = tmpObstacle
        else:
            matrix[position[0]:position[0]+tmpObstacle.shape[0], position[1]:position[1]+tmpObstacle.shape[1]] = -3
    matrix[matrix == -2] = 0
    matrix[matrix == -1] = 0
    matrix[matrix == -3] = -1
    return matrix

#function to calculate the cost of the index
def calculateCost(pMatrix, rMatrix):
    refMatrix = copy.deepcopy(pMatrix)
    countRow = 0
    countColumn = 0

    for row in refMatrix:
        for column in row:
            refMatrix[countRow%rMatrix][countColumn%rMatrix] = column[0] + column[1]
            countColumn += 1
        countRow += 1

    return refMatrix


#function to calculate the Manhattan distance for each node in the matrix
#Reminder Manhattan distance if | Xb - Xa | + | Yb - Ya |
#pMatrix : Matrice 
#rMatrix : Number of matrix's rows
#pEnd : The ending point ( the point from which we will calcul the manhattan distance )
def calculateManhattanDistance(pMatrix, rMatrix, pEnd):
    refMatrix = copy.deepcopy(pMatrix)
    countRow = 0
    countColumn = 0

    Xb = pEnd[0]
    Yb = pEnd[1]

    for row in refMatrix:
        for column in row:
            refMatrix[countRow%rMatrix][countColumn%rMatrix] = abs(Xb - column[0]) + abs(Yb - column[1]) 
            countColumn += 1
        countRow += 1
    return refMatrix

#Function add Cost matrix and Manhattant matrix
def addMatrixCostManhattan(pMatrixLeft, pMatrixRight, rMatrix):
    refMatrixLeft = copy.deepcopy(pMatrixLeft)
    refMatrixRight = copy.deepcopy(pMatrixRight)
    countRow = 0
    countColumn = 0


    for row in refMatrixLeft:
        for column in row:
            refMatrixLeft[countRow%rMatrix][countColumn%rMatrix] += refMatrixRight[countRow%rMatrix][countColumn%rMatrix]
            refMatrixLeft[countRow%rMatrix][countColumn%rMatrix] += refMatrixRight[countRow%rMatrix][countColumn%rMatrix]
            countColumn += 1
        countRow += 1

    return refMatrixLeft

#Function to find the better path with matrix
def pathfindingMatrix4direction(pMatrix, pComputedMatrix, rMatrix, pEnd):
    #Begin location
    Xa = 0
    Ya = 0
    #Path returned
    path = []
    #While not arrived 
    while not ((pEnd[0] == Xa) and (pEnd[1] == Ya)):
        #Buffer for the lowest value between the cross searching
        bufferLowest = -1
        #Cross searching values
        bXaPlus1 = -1
        bXaMinus1 = -1
        bYaPlus1 = -1
        bYaMinus1 = -1

        try:
            if (Xa + 1) < rMatrix:
                bXaPlus1 = pComputedMatrix[Ya][Xa + 1]
            else:
                bXaPlus1 = -1
        except NameError:
            print("Index out of bound : Ya = " + str(Ya) + "| Xa + 1 = "+ str(Xa + 1))

        try:
            if (Xa - 1) >= 0:
                bXaMinus1 = pComputedMatrix[Ya][Xa - 1]
            else:
                bXaMinus1 = -1
        except NameError:
            print("Index out of bound : Ya = " + str(Ya) + "| Xa - 1 = "+ str(Xa - 1))

        try:
            if (Ya + 1) < rMatrix:
                bYaPlus1 = pComputedMatrix[Ya + 1][Xa]
            else:
                bYaPlus1 = -1
        except NameError:
            print("Index out of bound : Ya + 1= " + str(Ya+1) + "| Xa = "+ str(Xa))
        
        try:
            if (Ya - 1) >= 0 :
                bYaMinus1 = pComputedMatrix[Ya - 1][Xa]
            else:
                bYaMinus1 = -1
        except NameError:
            print("Index out of bound : Ya = " + str(Ya-1) + "| Xa = "+ str(Xa) )
        
        #Counter loop = 0 / 1 / 2 / 3
        bArrayCross = [bXaPlus1, bXaMinus1, bYaPlus1, bYaMinus1]
        counterLoop = -1
        print(bArrayCross)

        for crossValue in bArrayCross:
            if bufferLowest > crossValue and crossValue > 0 or bufferLowest == -1:
                bufferLowest = crossValue
                counterLoop += 1

        if counterLoop == 0:
            path.append(pMatrix[Ya][Xa+1])
            Xa = Xa+1
        elif counterLoop == 1:
            path.append(pMatrix[Ya][Xa-1])
            Xa = Xa-1
        elif counterLoop == 2:
            path.append(pMatrix[Ya+1][Xa])
            Ya = Ya+1
        elif counterLoop == 3:
            path.append(pMatrix[Ya-1][Xa])
            Ya = Ya-1
    
    print(path)

    return path


#Globals
rMatrix = 20
matrix = createMatrix(rMatrix)
#print(matrix)
#listObstacle = [[1,0],[1,1],[0,3],[1,3],[2,3],[3,1],[3,2]]
#createObstacle(listObstacle, matrix)

#New function with a different methodology to create a A* algorithm
#Here's the different step to reach the goal :
# - Create a matrix with obstacle  
# - Evaluate the cost of all nodes
# - Algorithm of the A* search 
# Break out step by step of the algorithm :
# - Have an openlist which will contain all nodes that need to be evaluated 
# - Have a closelist which will contain all nodes already evaluated 
# - Core job
# --> Crawl the openlist until it's empty
# --> For each node crawled calculted f(n)
# --> Pick the node with the lowest f(n) cost  
# ----> Discover neighbors 
# ----> Evaluate the cost of neighbors 
def pathfindingAStar(positionStart, positionEnd, p_matrix):
    print("Start")
    openList = []
    closeList = []
    path = []

    StartNode = Node(positionStart, 
            ManhattanCost(positionStart[0],positionStart[1],positionEnd[0],positionEnd[0]),
            0,
            ManhattanCost(positionStart[0],positionStart[1],positionEnd[0],positionEnd[0]),
         [])

    openList.append(StartNode)

    cpt = 0
    while(len(openList) > 0):
        #The node with the lowest cost in the openlist
        currentNode = lowestFCost(openList)
        if(currentNode == -1):
            break
        #When the goal has been reach
        if currentNode.position == positionEnd:
            return currentNode
        #Looking for neighbors
        neighbors = findNeighbors(currentNode, p_matrix, positionEnd)
        #Adding neighbors to the open list
        for neighborNode in neighbors:
            openList.append(neighborNode)
        #Removing the explored node from the open list
        openList.remove(currentNode)
        #Search for node with the same parent as the current node and delete them from the open list
        currentNode = clearReplicate(currentNode, openList, closeList)
        #Adding the current node the close list
        closeList.append(currentNode)

        cpt += 1
        if cpt > 3000:
            print("Break")
            break
    
    return path

#Defining a type for nodes
@dataclass
class Node:
    position : list #Location in the matrix
    cost : float #The f cost
    costg: float 
    costh: float
    parents : list #The link to all parents
    

def ManhattanCost(Xa, Ya, Xb, Yb):
    return abs(Yb - Ya) + abs(Xa - Xb)

#Function that return the node with the lowest cost
def lowestFCost(openList):
    lowestNode = -1
    for Node in openList:
        if  lowestNode == -1 or Node.cost < lowestNode.cost:
            lowestNode = Node
        
    return lowestNode

#Function that will find neighbor nodes 
def findNeighbors(node :Node, matrix, positionEnd):
    #Variable that will return neighbors 
    neighbors = []
    #Possible move in the following order : down, right, up, left
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    for move in moves:
        #Storing new position
        movedPosition = [node.position[0] + move[0], node.position[1] + move[1]]
        #If position are in matrix range
        if movedPosition[0] < rMatrix and movedPosition[0] >= 0 and movedPosition[1] < rMatrix and movedPosition[1] >= 0:
            #Calulation of the manhattan cost 
            costh = ManhattanCost(movedPosition[0],movedPosition[1], positionEnd[0],positionEnd[1])
            costg = node.costg + 1
            if matrix[movedPosition[0]][movedPosition[1]] != -1:
                #Creation of the discovered node
                discoveredNode = Node(matrix[movedPosition[0]][movedPosition[1]],
                                        (costg + costh), #costf
                                        costg,
                                        costh,
                                            node)
                neighbors.append(discoveredNode)
    
    return neighbors

#Function that will search for the same nodes in the stack, and find for all of them find the parent 
#with the less f cost
def clearReplicate(currentNode :Node, openList, closeList):
    copyCurrentNode = copy.deepcopy(currentNode)
    for node in openList:
        if copyCurrentNode.position == node.position:
            if copyCurrentNode.cost > node.cost:
                copyCurrentNode.parents = node.parents
            openList.remove(node)
            closeList.append(node)
    return copyCurrentNode


#Function to print clearly the path from the start to the end
def printPath(node :Node):
    #Return value 
    path = []

    while node.parents != []:
        path.insert(0,node.position)
        node = node.parents
    path.insert(0, node.position)

    return path

#Function to inject obstacle inside an array matrix 
def injectObstacleFromNumpyMatrix(p_matrix, p_matrixObstacle):
    matrixObstacle = np.asarray(p_matrixObstacle)
    cptRow = 0
    cptColumn = 0
    if(len(matrixObstacle) == len(p_matrix)):
        for row in p_matrix:
            cptColumn = 0
            for column in row:
                if matrixObstacle[cptRow][cptColumn] == -1:
                    p_matrix[cptRow][cptColumn] = matrixObstacle[cptRow][cptColumn]
                cptColumn = cptColumn + 1
            cptRow = cptRow + 1
    





#Function that will simulate a traffic light crossroad
def trafficLightCrossroad(position):
    #Possible index to tag as a part of the crossroad : down, right, up, left
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    for move in moves:
        #Storing new position
        movedPosition = [position[0] + move[0], position[1] + move[1]]
        #If in matrix range
        #if movedPosition[0] < rMatrix and movedPosition[0] >= 0 and movedPosition[1] < rMatrix and movedPosition[1] >= 0: