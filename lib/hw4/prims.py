import sys # Library for INT_MAX 

class Graph():



    Queue mst = new Queue()

    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def primMST(self):
        Queue mst = new Queue()
        marked = True
        unmarked = False
        while not pq.isEmpty() and  self.size < graph.V()-1:
            e = pq.delMin()
            v = e.either()
            if marked[v] and marked [w]:
                mst.enqueue(e)
                if not marked[w]:
                    visit(graph,w)
                if not marked[v]:
                    visit(graph,v)

    	return 1