
from components.nodes import Node
from components.edges import Edge, TemporalEdge, Edges, TemporalEdges



class Arc(Edge):
    """
        A class which represents a directed edge (arc) on a graph.
    """

    def __init__(self, source, sink, nodes):
        super().__init__(source, sink, nodes)
        self.directed = True
        self.source = nodes.add(source)
        self.sink = nodes.add(sink)
        


class TemporalArc(TemporalEdge):
    """
        A class which represents a time-respecting directed edge (arc) on a temporal graph.
    """

    def __init__(self, source, sink, nodes, time, duration=1):
        super().__init__(source, sink, nodes, time, duration)
        self.directed = True
        self.source = nodes.add(source)
        self.sink = nodes.add(sink)
        


class Arcs(Edges):
    """
        A class which represents a collection of arcs.
    """

    def __init__(self):
        super().__init__()


    def add(self, source, sink, nodes):
        label = source + sink
        if not self.exists(label):
            self.set.add(Arc(source, sink, nodes))
        return self.get(label)


    def subset(self, alist):
        subset = Arcs()
        for edge in alist:
            subset.set.add(edge)
        return subset


    def get_edge_by_source(self, label):
        return self.subset([edge for edge in self.set if edge.source.label == label])


    def get_edge_by_sink(self, label):
        return self.subset([edge for edge in self.set if edge.sink.label == label])



class TemporalArcs(TemporalEdges):
    """
        A class which represents a collection of temporal arcs.
    """

    def __init__(self):
        super().__init__()


    def add(self, source, sink, nodes, time, duration=1):
        uid = source + sink + str(time)
        if not self.exists(uid):
            edge = TemporalArc(source, sink, nodes, time, duration)
            self.set.add(edge)
            self.stream.append(edge)
            self.streamsort()
        return self.get_edge_by_uid(uid)


    def subset(self, alist):
        subset = TemporalArcs()
        for edge in alist:
            subset.set.add(edge)
            subset.stream.append(edge)
        self.streamsort()
        return subset


    def get_edge_by_source(self, label):
        return self.subset([edge for edge in self.stream if edge.source.label == label])


    def get_edge_by_sink(self, label):
        return self.subset([edge for edge in self.stream if edge.sink.label == label])


    def get_edge_by_uid(self, uid):
        return next((edge for edge in self.set if edge.uid == uid), None)


    def exists(self, uid):
        return True if self.get_edge_by_uid(uid) is not None else False


    def uids(self):
        return [edge.uid for edge in self.stream]

    
    def print(self):
        print("\n{:5} {}".format(" ", " ".join(self.labels())) )
        for i in self.active_times():
            active = self.get_edge_by_time(i).labels()
            row = ['-']*len(self.labels())
            for label in active:
                index = self.labels().index(label)
                row[index] = '+'
            print("{:3} | {:2}".format(i, "  ".join(map(str, row))) )
        print()
