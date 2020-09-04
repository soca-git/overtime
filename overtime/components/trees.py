
from overtime.components.digraphs import TemporalDiGraph
from overtime.components.nodes import ForemostNodes
from overtime.components.arcs import TemporalArcs



class ForemostTree(TemporalDiGraph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, root, start):
        label = label + ' foremost tree [root: ' + root + ']'
        super().__init__(label)
        self.nodes = ForemostNodes(self)
        self.edges = TemporalArcs(self)
        self.root = self.nodes.add(root, self, start)
