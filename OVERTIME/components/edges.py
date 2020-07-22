
from components.nodes import Node, Nodes



class Edge:
    """
        A class which represents an edge on a graph.
    """

    def __init__(self, node1, node2, nodes):
        self.label = node1 + node2
        self.directed = False
        self.node1 = nodes.add(node1)
        self.node2 = nodes.add(node2)
        


class TemporalEdge(Edge):
    """
        A class which represents a time-respecting edge on a temporal graph.
    """

    def __init__(self, node1, node2, nodes, time, duration=1):
        super().__init__(node1, node2, nodes)
        self.uid = node1 + node2 + str(time)
        self.time = int(time)
        self.duration = int(duration)



class Edges:
    """
        A class which represents a collection of edges.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed collection of edge objects


    def add(self, node1, node2, nodes):
        label = node1 + node2
        if not self.exists(label):
            self.set.add(Edge(node1, node2, nodes))
        return self.get(label)


    def subset(self, alist):
        subset = Edges()
        for edge in alist:
            subset.set.add(edge)
        return subset


    def get(self, label):
        return next((edge for edge in self.set if edge.label == label), None)


    def get_edge_by_node1(self, label):
        return self.subset([edge for edge in self.set if edge.node1.label == label])


    def get_edge_by_node2(self, label):
        return self.subset([edge for edge in self.set if edge.node2.label == label])


    def exists(self, label):
        return True if self.get(label) is not None else False

    
    def count(self):
        return len(self.set)


    def labels(self):
        return [node.label for node in self.set]

    
    def print(self):
        print("\n{:5} edges;\n{:5} {}\n".format(self.count(), " ", " ".join(self.labels())) )



class TemporalEdges(Edges):
    """
        A class which represents a collection of temporal edges.
    """

    def __init__(self):
        super().__init__()
        self.stream = [] # ordered (by time), indexed collection of edge objects


    def add(self, node1, node2, nodes, time, duration=1):
        uid = node1 + node2 + str(time)
        if not self.exists(uid):
            edge = TemporalEdge(node1, node2, nodes, time, duration)
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


    def get_edge_by_node1(self, label):
        return self.subset([edge for edge in self.stream if edge.node1.label == label])


    def get_edge_by_node2(self, label):
        return self.subset([edge for edge in self.stream if edge.node2.label == label])


    def get_edge_by_uid(self, uid):
        return next((edge for edge in self.set if edge.uid == uid), None)


    def get_edge_by_time(self, time):
        return self.subset([edge for edge in self.set if edge.time == time])


    def get_edge_by_interval(self, interval):
        edges = []
        for time in interval:
            edges = edges + [edge for edge in self.stream if edge.time == time]
        return self.subset(edges)


    def streamsort(self):
        # look at operator.attrgetter for getting time from edge (optimized)
        self.stream = sorted(self.stream, key=lambda x:x.time, reverse=False)


    def exists(self, uid):
        return True if self.get_edge_by_uid(uid) is not None else False


    def uids(self):
        return [edge.uid for edge in self.stream]


    def labels(self):
        return list(set([node.label for node in self.stream]))


    def times(self):
        return [edge.time for edge in self.stream]


    def active_times(self):
        return list(set(self.times()))


    def firsttime(self):
        return self.stream[0].time
    

    def lifetime(self):
        return self.stream[-1].time + 1


    def timespan(self):
        return range(self.firsttime(), self.lifetime())

    
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
