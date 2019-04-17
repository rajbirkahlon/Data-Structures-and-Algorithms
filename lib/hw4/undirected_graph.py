class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        
        return 1
        
    def add_neighbors(self, neighbors):
        
        return 1
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        return 1

            
    def add_vertices(self, vertices):
        self.vertices.appen(vertices)
        return 1 
            
    def add_edge(self, vertex_from, vertex_to):
        vertex_from.add_vertex(vertex_to)
        vertex_to.add_vertex(vertex_from)
        return 1 
                
    def add_edges(self, edges):
        
        return 1         
    
    def adjacencyList(self): # to represent the graph as adjacent list  
        
        return 1           
                        
def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n'