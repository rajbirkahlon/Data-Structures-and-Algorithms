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


    	return 1


   	def SCC(self):    # strongly connected components

   		return 1