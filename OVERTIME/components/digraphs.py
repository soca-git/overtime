
from components.graphs import Graph, TemporalGraph
from components.nodes import Nodes
from components.arcs import Arcs, TemporalArcs



class DiGraph(Graph):
    """
        A class which represents a graph consisting of nodes & arcs.
    """

    def __init__(self, label):
        super().__init__(label)
        self.directed = True
        self.edges = Arcs()
        


class TemporalDiGraph(TemporalGraph):
    """
        A class which represents a temporal graph consisting of nodes & temporal arcs.
    """

    def __init__(self, label):
        super().__init__(label)
        self.directed = True
        self.edges = TemporalArcs()
