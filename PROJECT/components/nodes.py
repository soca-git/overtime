
class Node:
    """
        A class which represents a node on a graph.
    """

    def __init__(self, label):
        self.label = label



class Nodes:
    """
        A class which represents a collection of nodes.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed, unique collection of node objects
        self.labels = set() # unorderd, unindexed, unique collection of node labels

    def add(self, node):
        if node.label not in self.labels:
            self.set.add(node)
        self.labels.add(node.label)
