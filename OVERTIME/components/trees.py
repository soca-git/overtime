
from components.graphs import TemporalGraph
from components.nodes import ForemostNodes
from components.edges import TemporalEdges



class ForemostTree(TemporalGraph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, root, start):
        self.label = label + ' foremost tree [root: ' + root + ']'
        self.nodes = ForemostNodes()
        self.edges = TemporalEdges()
        self.root = self.nodes.add(root, start)
