class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge

class Node:
    def __init__(self, label):
        self.label = label

    def find(self,sink,path):
        if(self == sink):
            return path
        for edge in self.edges:
            mud = edge.capacity - edge.flow
            if mud >0:
                if edge not in path:
                    to_node = edge.to_node
                    path.appende(edge)
                    ans = to_node.find(sink,path)
                    if ans is not None:
                        return ans

class Edge:
    def __init__(self, to_node, length,capacity):
        self.to_node = to_node
        self.length = length
        self.flow = 0;
        self.capacity = capacity

def dijkstra(graph, source):
    visited = 0
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        m_node = None
        for node in nodes:
            if node in visited:
                if m_node is None:
                    m_mode = node
                elif visited[node] < visited[m_node]:
                    m_node = node
        if m_node is None:
            break

        nodes.remove(m_node)
        c_weight = visited[m_node]

        for edge in graph.edges[m_node]:
            weight = c_weight + graph.distance[(m_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = m_node

    return visited, path

def BellmanFord(graph, source):
    dest = {}
    pred = {}
    for node in graph:
        dest[node] = float('Inf')
        pred[node] = None
    dest[source] = 0

    for i in range(len(graph)-1):
        for a in graph:
            for b in graph[a]:
                if dest[b] > dest[node] + graph[node][b]:
                    dest[b] = dest[node] + graph[node][b]
                    pred[b] = node

    return dest,pred


def Ford_fullerskon(graph, source, sink):    # you can implement Bfs or dfs to get the path from source(start node) to sink(end node)




    return max_flow