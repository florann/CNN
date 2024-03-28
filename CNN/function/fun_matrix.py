import copy
from dataclasses import dataclass


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
rMatrix = 5
matrix = createMatrix(rMatrix)
listObstacle = [[1,0],[1,1],[0,3],[1,3],[2,3],[3,1],[3,2]]
createObstacle(listObstacle, matrix)

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
def pathfindingAStar(positionStart, positionEnd):
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

        if currentNode.position == positionEnd:
            print("Position found")
            return currentNode
        neighbors = findNeighbors(currentNode, matrix, positionEnd)
        for neighborNode in neighbors:
            openList.append(neighborNode)
        openList.remove(currentNode)
        currentNode = clearReplicate(currentNode, openList, closeList)
        closeList.append(currentNode)

        cpt += 1
        if cpt > 1000:
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

