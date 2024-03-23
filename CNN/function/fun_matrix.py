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
def calculateCost(pMatrix):
    refMatrix = copy.deepcopy(pMatrix)
    countRow = 0
    countColumn = 0

    for row in refMatrix:
        for column in row:
            refMatrix[countRow%4][countColumn%4] = column[0] + column[1]
            countColumn += 1
        countRow += 1

    return refMatrix
