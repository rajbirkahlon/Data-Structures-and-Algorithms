import sys # Library for INT_MAX 

class Graph():
    Queue mst = new Queue()

    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def primMST(self):
        Edge e = pq.delMin()

    	return 1