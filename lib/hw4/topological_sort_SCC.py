import sys
from collections import defaultdict
from queue import *

  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def topological_Sort(self):
        PQ = Queue(maxsize=100)
        ranks = self.V
        order = PQ
        for a in Graph:
            self.in_deg[a] = 0
            for a in Graph:
                for b in Graph[a]:
                    self.in_deg[b] = self.in_deg[b]+1

        Q = self.deque()
        for a in self.in_deg:
            if self.in_deg[a] == 0:
                Q.append()

        L = []
        a = Q.pop()
        L.append[a]
        for b in Graph[a]:
            self.in_deg[b] = self.in_deg[b]-1
            if self.in_deg[b] == 0:
                Q.append()

        return L

   	def SCC(self):    # strongly connected components

   		return 1