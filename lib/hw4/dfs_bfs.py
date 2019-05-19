from collections import defaultdict 

class Graph:
	def __init__(self): 
		self.graph = defaultdict(list)
		return

	def addEdge(self,u,v):
		if v not in self.nodes:
			self.add_node(v)
			self.nodes[v].add_neighbor(self.nodes[u])
		if u not in self.nodes:
			self.add_node(u)
			self.nodes[u].add_neighbor(self.nodes[v])
		if u not in self.nodes and v not in self.nodes:
			self.add_node(u)
			self.add_node(v)
			self.nodes[v].add_neighbor(self.nodes[u])
			self.nodes[u].add_neighbor(self.nodes[v])

def dfs(self, v):



    	return 1

   	def bfs(self, v):



		return 1
