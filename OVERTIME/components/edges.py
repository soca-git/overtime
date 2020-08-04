
from components.nodes import Node, Nodes



class Edge:
    """
        A class which represents an edge on a graph.
    """

    def __init__(self, node1, node2, nodes, graph):
        self.label = str(node1) + str(node2)
        self.uid = self.label
        self.directed = False
        self.node1 = nodes.add(node1, graph)
        self.node2 = nodes.add(node2, graph)
        self.graph = graph
        

    def print(self):
        print(self.label)



class TemporalEdge(Edge):
    """
        A class which represents a time-respecting edge on a temporal graph.
    """

    def __init__(self, node1, node2, nodes, graph, tstart, tend):
        super().__init__(node1, node2, nodes, graph)
        self.uid = str(node1) + str(node2) + str(tstart) + str(tend)
        self.start = int(tstart)
        self.end = int(tend)
        self.duration = self.end - self.start + 1

    
    def is_active(self, time):
        return True if time >= self.start and time <= self.end else False


    def print(self):
        print(self.uid)



class Edges:
    """
        A class which represents a collection of edges.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed collection of edge objects

    
    def aslist(self):
        return list(self.set)


    def add(self, node1, node2, nodes, graph):
        node_labels = sorted([str(node1),str(node2)])
        label = '-'.join(node_labels) # alphabetically sorted label
        if not self.exists(label):
            self.set.add(Edge(node_labels[0], node_labels[1], nodes, graph))
        return self.get_edge_by_uid(label)


    def subset(self, alist):
        subset = Edges()
        for edge in alist:
            subset.set.add(edge)
        return subset

    
    def get_edge_by_uid(self, uid):
        return next((edge for edge in self.set if edge.uid == uid), None)


    def get_edge_by_label(self, label):
        return self.subset(edge for edge in self.set if edge.label == label)


    def get_edge_by_node(self, label):
        return self.subset(edge for edge in self.set if edge.node1.label == label or edge.node2.label == label)


    def get_edge_by_node1(self, label):
        return self.subset([edge for edge in self.set if edge.node1.label == label])


    def get_edge_by_node2(self, label):
        return self.subset([edge for edge in self.set if edge.node2.label == label])


    def exists(self, uid):
        return True if self.get_edge_by_uid(uid) is not None else False

    
    def count(self):
        return len(self.set)


    def uids(self):
        return [edge.uid for edge in self.set]


    def labels(self):
        return [edge.label for edge in self.set]

    
    def ulabels(self):
        return list(set([edge.label for edge in self.set]))

    
    def print(self):
        print('Edges:')
        for edge in self.set:
            edge.print()



class TemporalEdges(Edges):
    """
        A class which represents a collection of temporal edges.
    """

    def __init__(self):
        super().__init__()
        self.set = [] # ordered (by time), indexed collection of edge objects


    def add(self, node1, node2, nodes, graph, tstart, tend=None):
        if tend is None:
            tend = int(tstart) + 0 # default duration of 1
        node_labels = sorted([str(node1),str(node2)])
        uid = '-'.join(node_labels) + '|' + str(tstart) + '-' + str(tend) # uid is alphabetically sorted
        if not self.exists(uid):
            edge = TemporalEdge(node_labels[0], node_labels[1], nodes, graph, tstart, tend)
            self.set.append(edge)
            self.set = self.setsort()
        return self.get_edge_by_uid(uid)


    def subset(self, alist):
        subset = TemporalEdges()
        for edge in alist:
            subset.set.append(edge)
        subset.set = subset.setsort()
        return subset


    def get_edge_by_start(self, time):
        return self.subset([edge for edge in self.set if edge.start == time])

    
    def get_edge_by_end(self, time):
        return self.subset([edge for edge in self.set if edge.end == time])


    def get_edge_by_interval(self, interval):
        return self.subset([edge for edge in self.set if edge.start >= interval[0] and edge.start < interval[1]])


    def get_active_edges(self, time):
        return self.subset(edge for edge in self.set if edge.is_active(time))


    def setsort(self, key='start'):
        if key is 'end':
            return sorted(self.set, key=lambda x:x.end, reverse=False)
        elif key is 'start':
            # look at operator.attrgetter for getting start time from edge (optimized)
            return sorted(self.set, key=lambda x:x.start, reverse=False)
        

    def start_times(self):
        return [edge.start for edge in self.set]

    
    def end_times(self):
        return [edge.end for edge in self.set]


    def start(self):
        return self.set[0].start
    

    def end(self):
        return self.setsort()[-1].end + 1


    def timespan(self):
        return range(self.start(), self.end())

    
    def print(self):
        print('Edges:')
        print("\n{:5} {}".format(" ", " ".join(self.ulabels())) )
        for t in self.timespan():
            active = self.get_active_edges(t).ulabels()
            row = ['-']*len(self.ulabels())
            for label in active:
                index = self.ulabels().index(label)
                row[index] = '+'
            print("{:3} | {:2}".format(t, "  ".join(map(str, row))) )
        print()
