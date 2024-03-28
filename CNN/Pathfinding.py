#import numpy to create matrix easily 
import numpy as np
import threading as th
import concurrent.futures as ThreadManager
 

from function.fun_matrix import *

#Equivalent of the main function
#pathfindingAStar(matrix[0][0], matrix[4][4])

with ThreadManager.ThreadPoolExecutor() as executor:
    #Starting threads with a pathfinding calculation
    returnValue1 = executor.submit(pathfindingAStar, matrix[0][0],matrix[4][4])
    returnValue2 = executor.submit(pathfindingAStar, matrix[0][0],matrix[0][4])

    print(returnValue1.result())
    print(returnValue2.result())


