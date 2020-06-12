


class Edge:
    """
        A class which represents an edge on a graph.
    """

    def __init__(self, label, source, sink):
        self.label = label
        self.source = source
        self.sink = sink



class TemporalEdge(Edge):
    """
        A class which represents a time-respecting edge on a temporal graph.
    """

    def __init__(self, label, source, sink, time):
        self.time = time



class Edges:
    """
        A class which represents a collection of edges.
    """

    def __init__(self):
        self.list = [] # unorderd, indexed collection of edge objects
        self.stream = [] # ordered, indexed collection of edge objects
        self.labels = set() # unorderd, unindexed, unique collection of edge labels

    def add(self, edge):
        self.list.append(edge)
        self.labels.add(edge.label)
        self.stream.append(edge)
        self.streamsort

    def streamsort(self):
        # look at operator.attrgetter for getting time from edge (optimized)
        self.stream = sorted(self.stream, key=lambda x:x.time, reverse=True)
