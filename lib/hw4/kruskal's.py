from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 


    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 


    def KruskalMST(self):

    	return 1