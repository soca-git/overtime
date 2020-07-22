
class Node:
    """
        A class which represents a node on a graph.
    """

    def __init__(self, label):
        self.label = label
        self.data = dict()


    def print(self):
        print(self.label)



class ForemostNode(Node):
    """
        A class which represent a node on a foremost tree.
    """

    def __init__(self, label, time=float('inf')):
        super().__init__(label)
        self.time = time


    def print(self):
        print(self.label, self.time)



class Nodes:
    """
        A class which represents a collection of nodes.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed, unique collection of node objects


    def add(self, label):
        if not self.exists(label):
            self.set.add(Node(label))
        return self.get(label)


    def get(self, label):
        return next((node for node in self.set if node.label == label), None)


    def exists(self, label):
        return True if self.get(label) is not None else False

    
    def count(self):
        return len(self.set)


    def labels(self):
        return [node.label for node in self.set]


    def print(self):
        print('Nodes:')
        for node in self.set:
            node.print()


class ForemostNodes(Nodes):
    """
        A class which represents a collection of foremost nodes.
    """

    def __init__(self):
        super().__init__()


    def add(self, label, time=float('inf')):
        if not self.exists(label):
            self.set.add(ForemostNode(label, time))
        return self.get(label)
