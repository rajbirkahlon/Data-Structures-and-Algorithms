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

class Digraph:
    """This class implements a directed graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.edges = 0

    def add_node(self, node):
        """adds vertices to your graph"""
        new_node = Vertex(node)
        self.nodes[node] = new_node
        return 1
    def add_edge(self, last, first):
        """creates edges between two given vertices in your graph"""
        if last not in self.nodes:
            self.add_node(last)
            self.nodes[last].add_neighbor(self.nodes[first])
        else:
            self.add_node(first)
            self.nodes[first].add_neighbor(self.nodes[last])

        return 1

    def has_edge(self, first, last):   
        """checks if a connection exists between two given nodes in your graph"""
        if self.nodes[first].neighbor == last or self.nodes[last].neighbor == first:
            return True
        else:
            return False

    def remove_edge(self, last, first):
        """removes edges between two given vertices in your graph"""
        if last not in self.nodes:
            self.nodes[last].neighbor = None
        else:
            self.nodes[first].neighbor = None

        return 1


    def remove_node(self, node):
        """removes vertices from your graph"""
        self.nodes[node] = None
        return 1

    def contains(self, node):
        """checks if your graph contains a given value"""
        for i in range(len(self.nodes)):
            if self.nodes[i] == node:
                return True
        return False

