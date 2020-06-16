


class Graph:
    """
        A class which represents a graph consisting of nodes & edges.
    """

    def __init__(self, label, nodes, edges):
        self.label = label
        self.nodes = nodes
        self.edges = edges



class TemporalGraph(Graph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """
