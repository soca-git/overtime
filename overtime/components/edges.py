
from overtime.components.nodes import Node, Nodes



class Edge:
    """
        A class which represents an edge on a graph.
    """

    def __init__(self, node1, node2, nodes):
        self.label = str(node1) + '-' + str(node2)
        self.uid = self.label
        self.directed = False
        self.node1 = nodes.add(node1)
        self.node2 = nodes.add(node2)
        self.graph = nodes.graph
        

    def print(self):
        print(self.label)



class TemporalEdge(Edge):
    """
        A class which represents a time-respecting edge on a temporal graph.
    """

    def __init__(self, node1, node2, nodes, tstart, tend):
        super().__init__(node1, node2, nodes)
        self.uid = str(node1) + str(node2) + str(tstart) + str(tend)
        self.start = int(tstart)
        self.end = int(tend)
        self.duration = self.end - self.start + 1

    
    def isactive(self, time):
        return True if time >= self.start and time <= self.end else False


    def print(self):
        print(self.uid)



class Edges:
    """
        A class to represent a collection of edges on a graph.

        Parameter(s):
        -------------
        graph : Graph
            A valid Graph class/subclass.


        Object Propertie(s):
        --------------------
        set : Set
            The set of nodes.
        graph : Graph
            The graph of which the edges collection belongs to.


        See also:
        ---------
            Edge
            TemporalEdge
            TemporalEdges
    """

    def __init__(self, graph):
        self.set = set() # unorderd, unindexed collection of edge objects
        self.graph = graph

    
    def aslist(self):
        return list(self.set)


    def add(self, node1, node2, nodes):
        """
            A method of Edges.

            Parameter(s):
            -------------
            node1 : String
                The label of the node1 connection.
            node2 : String
                The label of the node2 connection.
            node : Nodes
                A valid Nodes class/subclass.

            Returns:
            --------
            edge : Edge
                The corresponding edge object.
        """
        node_labels = sorted([str(node1),str(node2)])
        label = '-'.join(node_labels) # alphabetically sorted label
        if not self.exists(str(label)):
            self.set.add(Edge(node_labels[0], node_labels[1], nodes))
        return self.get_edge_by_uid(label)


    def remove(self, label):
        """
            A method of Nodes.

            Parameter(s):
            -------------
            label : String
                The label of the node to be removed.
            graph : Graph
                A valid Graph class/subclass.

            Returns:
            --------
            None, removes the node if it exists in the graph.
        """
        # check if a node with this label already exists in the graph.
        if not self.exists(str(label)):
            print('Error: {} not found in graph {}.'.format(label, self.graph.label))
        else:
            self.set.remove(self.get_edge_by_uid(label))
            print('{} removed from graph {}.'.format(label, self.graph.label))


    def subset(self, alist):
        subset = Edges(self.graph)
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

    def __init__(self, graph):
        super().__init__(graph)
        self.set = [] # ordered (by time), indexed collection of edge objects


    def add(self, node1, node2, nodes, tstart, tend=None):
        """
            A method of TemporalEdges.

            Parameter(s):
            -------------
            node1 : String
                The label of the node1 connection.
            node2 : String
                The label of the node2 connection.
            nodes : Nodes
                A valid Nodes class/subclass.
            tstart : Integer
                The start time of the temporal edge.
            tend : Integer
                The end time of the temporal edge.

            Returns:
            --------
            edge : TemporalEdge
                The corresponding edge object.
        """
        if tend is None:
            tend = int(tstart) + 0 # default duration of 0
        node_labels = sorted([str(node1),str(node2)])
        uid = '-'.join(node_labels) + '|' + str(tstart) + '-' + str(tend) # uid is alphabetically sorted
        if not self.exists(uid):
            edge = TemporalEdge(node_labels[0], node_labels[1], nodes, tstart, tend)
            self.set.append(edge)
            self.set = self.setsort(self.set)
        return self.get_edge_by_uid(uid)


    def subset(self, alist):
        subset = TemporalEdges(self.graph)
        for edge in alist:
            subset.set.append(edge)
        subset.set = subset.setsort(subset.set)
        return subset


    def get_edge_by_start(self, time):
        return self.subset([edge for edge in self.set if edge.start == time])

    
    def get_edge_by_end(self, time):
        return self.subset([edge for edge in self.set if edge.end == time])


    def get_edge_by_interval(self, interval):
        return self.subset([edge for edge in self.set if edge.start >= interval[0] and edge.start < interval[1]])


    def get_active_edges(self, time):
        return self.subset(edge for edge in self.set if edge.isactive(time))


    def setsort(self, aset, key='start'):
        if key is 'end':
            return sorted(aset, key=lambda x:x.end, reverse=False)
        elif key is 'start':
            # look at operator.attrgetter for getting start time from edge (optimized)
            return sorted(aset, key=lambda x:x.start, reverse=False)


    def ulabels(self):
        return sorted(set([label for label in self.labels()]), key=lambda x:self.labels().index(x))
        

    def start_times(self):
        return [edge.start for edge in self.set]

    
    def end_times(self):
        return [edge.end for edge in self.set]


    def start(self):
        return self.set[0].start
    

    def end(self):
        return self.set[-1].end + 1


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
