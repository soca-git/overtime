
from overtime.components.graphs import TemporalGraph
from overtime.components.nodes import ForemostNodes
from overtime.components.arcs import TemporalArcs



class ForemostTree(TemporalGraph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, root, start):
        label = label + ' foremost tree [root: ' + root + ']'
        super().__init__(label)
        self.nodes = ForemostNodes()
        self.edges = TemporalArcs()
        self.root = self.nodes.add(root, self, start)
