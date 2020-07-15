
from components.graphs import TemporalGraph
from components.nodes import ForemostNode, ForemostNodes
from components.edges import TemporalEdges



class ForemostTree(TemporalGraph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, root, start):
        self.nodes = ForemostNodes()
        self.edges = TemporalEdges()
        self.root = self.nodes.add(root, start)
