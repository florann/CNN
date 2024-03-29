#import numpy to create matrix easily 
import numpy as np
import threading as th
import concurrent.futures as ThreadManager
#importing function
from function.fun_matrix import *
#importing server
from Server.server import *

#Equivalent of the main function
#pathfindingAStar(matrix[0][0], matrix[4][4])
'''
hostName = "localhost"
serverPort = 8080

if __name__ == "__main__":        
    webServer = WebRequestHandler((hostName, serverPort), )
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
'''
    
with ThreadManager.ThreadPoolExecutor() as executor:
    #Starting threads with a pathfinding calculation
    returnValue1 = executor.submit(pathfindingAStar, matrix[8][0],matrix[8][19])
    returnValue2 = executor.submit(pathfindingAStar, matrix[0][8],matrix[19][8])

    print(printPath(returnValue1.result()))
    print(printPath(returnValue2.result()))


