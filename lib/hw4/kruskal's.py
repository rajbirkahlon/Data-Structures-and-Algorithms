from collections import defaultdict
import PriorityQueue
from hw1 import union_find.py

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
        mst = new Queue()
        pq = new MinPQ,(graph.V())
        uf = new UF(graph.V())
        while pq and  self.size < graph.V()-1:
            e = pq.delMin()
            v = e.either(), w = e.other(v)
            if(!connected()):
                uf.union(v,w)
                mst.enqueu(e)
    	return 1