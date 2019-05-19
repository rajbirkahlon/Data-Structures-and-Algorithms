import sys
from collections import defaultdict
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def topological_Sort(self):
        ranks = self.V
        order = PQ
        in_deg = {a = 0 for a in Graph}
            for a in Graph:
                for b in Graph[a]:
                    in_deg[b] = in_deg[b]+1

        Q = deque()
        for a in in_deg:
            if in_deg[a] == 0:
                Q.append()


        Q.append()


    	return 1


   	def SCC(self):    # strongly connected components

   		return 1