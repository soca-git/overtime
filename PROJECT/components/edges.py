


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

    def __init__(self, label, source, sink, active_times):
        self.activetimes = active_times
