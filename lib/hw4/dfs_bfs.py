from queue import *
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

   	def bfs(self, v):
		p = float('Inf')
		for i in range(len(self.graph)):
			self.distTo[i] = p
		self.distTo = 0
		self.marked[v] = True
		Queue.enqueue(v)

		while Queue:
			a = Queue.dequeue()
			for b in range(self.graph):
				self.edgeTo[b] = a
				self.distTo[b] = self.distTo[a]+1
				self.marked[b] = True
				Queue.enqueue(b)
		return 1

	def dfs(self, v):
		self.marked = True
		for i in range(Graph):
			if self.marked[i] == False:
				self.edgeTo[i] = v
				self.dfs(Graph,i)
    	return 1