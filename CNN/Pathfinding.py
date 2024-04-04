#import numpy to create matrix easily 
import numpy as np
import threading as th
import concurrent.futures as ThreadManager
#importing function
from PythonFunction.func_pathFinding import *

if __name__ == '__main__':
    app.run(debug=True)

with ThreadManager.ThreadPoolExecutor() as executor:
    #Starting threads with a pathfinding calculation
    returnValue1 = executor.submit(pathfindingAStar, matrix[8][0],matrix[8][19])
    returnValue2 = executor.submit(pathfindingAStar, matrix[0][8],matrix[19][8])

    print(printPath(returnValue1.result()))
    print(printPath(returnValue2.result()))


