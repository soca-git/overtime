
from components.nodes import Node

class Edge:
    """
        A class which represents an edge on a graph.
    """

    def __init__(self, source, sink, nodes):
        self.label = source + sink
        self.source = nodes.add(source)
        self.sink = nodes.add(sink)



class TemporalEdge(Edge):
    """
        A class which represents a time-respecting edge on a temporal graph.
    """

    def __init__(self, source, sink, nodes, time):
        super().__init__(source, sink, nodes)
        self.time = int(time)
        self.uid = source + sink + str(time)



class Edges:
    """
        A class which represents a collection of edges.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed collection of edge objects


    def add(self, source, sink, nodes):
        label = source + sink
        if not self.check(label):
            self.set.add(Edge(source, sink, nodes))
        return self.get(label)


    def subset(self, alist):
        subset = Edges()
        for edge in alist:
            subset.set.add(edge)
        return subset


    def get(self, label):
        return next((edge for edge in self.set if edge.label == label), None)


    def get_edge_by_source(self, label):
        return self.subset([edge for edge in self.set if edge.source.label == label])


    def get_edge_by_sink(self, label):
        return self.subset([edge for edge in self.set if edge.sink.label == label])


    def check(self, label):
        return True if self.get(label) is not None else False

    
    def count(self):
        return len(self.set)



class TemporalEdges(Edges):
    """
        A class which represents a collection of temporal edges.
    """

    def __init__(self):
        super().__init__()
        self.stream = [] # ordered (by time), indexed collection of edge objects


    def add(self, source, sink, nodes, time):
        uid = source + sink + str(time)
        if not self.check(uid):
            edge = TemporalEdge(source, sink, nodes, time)
            self.set.add(edge)
            self.stream.append(edge)
            self.streamsort()
        return self.get_edge_by_uid(uid)


    def subset(self, alist):
        subset = TemporalEdges()
        for edge in alist:
            subset.set.add(edge)
            subset.stream.append(edge)
        self.streamsort()
        return subset


    def get(self, label):
        return self.subset([edge for edge in self.set if edge.label == label])


    def get_edge_by_uid(self, uid):
        return next((edge for edge in self.set if edge.uid == uid), None)


    def get_edge_by_time(self, time):
        return self.subset([edge for edge in self.set if edge.time == time])


    def streamsort(self):
        # look at operator.attrgetter for getting time from edge (optimized)
        self.stream = sorted(self.stream, key=lambda x:x.time, reverse=False)


    def check(self, uid):
        return True if self.get_edge_by_uid(uid) is not None else False


    def uids(self):
        return [edge.uid for edge in self.stream]


    def get_labels(self):
        return [node.label for node in self.set]


    def get_times(self):
        return [edge.time for edge in self.stream]
