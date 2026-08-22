class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.coordinates = {}

    def add_node(self, name, x=0, y=0):
        if name not in self.adjacency_list:
            self.adjacency_list[name] = {}
        self.coordinates[name] = (x, y)

    def add_edge(self, node1, node2, weight):
        self.adjacency_list[node1][node2] = weight
        self.adjacency_list[node2][node1] = weight

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, {})

    def get_nodes(self):
        return list(self.adjacency_list.keys())