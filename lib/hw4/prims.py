import sys # Library for INT_MAX 
from queue import *
class Graph():




    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def primMST(self):
        mst = Queue(maxsize=20)
        pq = Queue(maxsize=19)
        marked = True
        unmarked = False
        while not pq.isEmpty() and  self.size < Graph.V()-1:
            e = pq.delMin()
            v = e.either()
            w = not e.either
            if marked[v] and marked [w]:
                mst.enqueue(e)
                if not marked[w]:
                    self.visit(Graph,w)
                if not marked[v]:
                    self.visit(Graph,v)

    	return 1