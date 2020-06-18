


class Node:
    """
        A class which represents a node on a graph.
    """

    def __init__(self, label):
        self.label = label
        self.sourceof = {}
        self.sinkof = {}



class Nodes:
    """
        A class which represents a collection of nodes.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed, unique collection of node objects


    def add(self, label):
        if not self.check(label):
            self.set.add(Node(label))
        return self.get(label)


    def get(self, label):
        return next((node for node in self.set if node.label == label), None)


    def check(self, label):
        return True if self.get(label) is not None else False

    
    def count(self):
        return len(self.set)


    def labels(self):
        return [node.label for node in self.set]


    def print(self):
        print("\n{:5} nodes;\n{:5} {}\n".format(self.count()," ", " ".join(self.labels())) )

