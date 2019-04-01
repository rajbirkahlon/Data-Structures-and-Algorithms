class Digraph:
    """This class implements a directed, weighted graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.children = dict()
        self.parents = dict()
        self.edges = 0

    def add_node(self, node):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""

        return 1
    def add_arc(self, tail, head, weight):
        """Creates a directed arc pointing from 'tail' to 'head' and assigns 'weight' as its weight."""
        
        return 1

    def has_arc(self, tail, head):
        

        return 1
    def get_arc_weight(self, tail, head):
        

        return 1

    def remove_arc(self, tail, head):
        """Removes the directed arc from 'tail' to 'head'."""
        
        return 1

    def remove_node(self, node):
        """Removes the node from this digraph. Also, removes all arcs incident on the input node."""
        
        return 1

    def __len__(self):
        
        return 1 

    def number_of_arcs(self):
        return 1

    def get_parents_of(self, node):
        """Returns all parents of 'node'."""
        return 1

    def get_children_of(self, node):
        """Returns all children of 'node'."""
        return 1

    def clear(self):
        del self.nodes[:]
        self.children.clear()
        self.parents.clear()
        self.edges = 0