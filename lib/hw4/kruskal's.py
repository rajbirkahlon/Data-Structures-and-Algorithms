from collections import defaultdict
from hw1 import union_find.py
from queue import *

#Class to represent a graph 
class Graph:


    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph
        self.size = 0

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
        self.size += 1


    def KruskalMST(self):
        mst = Queue(maxsize=20)
        pq = Queue(maxsize=20)
        uf = self.UF(Graph.V())
        while pq and  self.size < Graph.V()-1:
            e = pq.delMin()
            v = e.either()
            w = e.other(v)
            if not self.connected():
                uf.union(v,w)
                mst.enqueu(e)
    	return 1