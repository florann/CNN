import copy


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
            print("Index out of bound : Ya = " + Ya + "| Xa + 1 = "+ Xa + 1)

        try:
            if (Xa - 1) >= 0:
                bXaMinus1 = pComputedMatrix[Ya][Xa - 1]
            else:
                bXaMinus1 = -1
        except NameError:
            print("Index out of bound : Ya = " + Ya + "| Xa - 1 = "+ Xa - 1)

        try:
            if (Ya + 1) < rMatrix:
                bYaPlus1 = pComputedMatrix[Ya + 1][Xa]
            else:
                bYaPlus1 = -1
        except NameError:
            print("Index out of bound : Ya + 1= " + Ya+1 + "| Xa = "+ Xa)
        
        try:
            if (Ya - 1) >= 0 :
                bYaMinus1 = pComputedMatrix[Ya - 1][Xa]
            else:
                bYaMinus1 = -1
        except NameError:
            print("Index out of bound : Ya = " + Ya-1 + "| Xa = "+ Xa )
        
        #Counter loop = 0 / 1 / 2 / 3
        bArrayCross = [bXaPlus1, bXaMinus1, bYaPlus1, bYaMinus1]
        counterLoop = -1

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
        print(Ya)
        print(Xa)
        #break

    return path
