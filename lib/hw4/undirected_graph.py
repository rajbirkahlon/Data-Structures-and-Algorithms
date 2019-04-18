import sys
class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        self.dist = sys.maxint
        self.visited = False
        
    def add_neighbor(self, neighbor):
        self.adjacent[neighbor] = 0
        return 1
        
    def add_neighbors(self, neighbors):
        self.adjacent[neighbors] = 0
        return 1
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        new_v = Vertex(vertex)
        self.neighbors[vertex] = new_v
        return 1

            
    def add_vertices(self, vertices):
        #self.vertices.appen(vertices)
        return 1 
            
    def add_edge(self, vertex_from, vertex_to):
        if vertex_from not in self.vertices:
            self.add_vertex(vertex_from)
        if vertex_to not in self.vertices:
            self.add_vertex(vertex_to)
        return 1 
                
    def add_edges(self, edges):
        self.add_vertices(edges)
        return 1         
    
    def adjacencyList(self): # to represent the graph as adjacent list  
        return self.vertices
        return 1           
                        
def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n'