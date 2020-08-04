
class Node:
    """
        A class which represents a node on a graph.
    """

    def __init__(self, label, graph):
        self.label = str(label)
        self.graph = graph
        self.data = dict()


    def print(self):
        print(self.label)


    def node1of(self, time=None):
        if time is not None:
            edges = self.graph.edges.get_edge_by_time(time)
        else:
            edges = self.graph.edges
        
        return edges.get_edge_by_node1(self.label)

    
    def sourceof(self, time=None):
        return self.node1of(time)


    def node2of(self, time=None):
        if time is not None:
            edges = self.graph.edges.get_edge_by_time(time)
        else:
            edges = self.graph.edges
        
        return edges.get_edge_by_node2(self.label)

    
    def sinkof(self, time=None):
        return self.node2of(time)


    def nodeof(self, time=None):
        if time is not None:
            edges = self.graph.edges.get_edge_by_time(time)
        else:
            edges = self.graph.edges
        
        return edges.get_edge_by_node(self.label)



    def neighbours(self, time=None):
        node1_edges = self.node1of(time)
        node2_edges = self.node2of(time)

        neighbours = self.graph.nodes.subset([])
        for edge in node1_edges.set:
            if not neighbours.exists(edge.node2.label):
                neighbours.add(edge.node2.label, self)
        for edge in node2_edges.set:
            if not neighbours.exists(edge.node1.label):
                neighbours.add(edge.node1.label, self)
        return neighbours



class ForemostNode(Node):
    """
        A class which represent a node on a foremost tree.
    """

    def __init__(self, label, graph, time=float('inf')):
        super().__init__(label, graph)
        self.time = time


    def print(self):
        print(self.label, self.time)



class Nodes:
    """
        A class which represents a collection of nodes.
    """

    def __init__(self):
        self.set = set() # unorderd, unindexed, unique collection of node objects


    def aslist(self):
        return list(self.set)


    def add(self, label, graph):
        if not self.exists(label):
            self.set.add(Node(label, graph))
        return self.get(label)


    def subset(self, alist):
        subset = Nodes()
        for node in alist:
            subset.set.add(node)
        return subset


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


    def add(self, label, graph, time=float('inf')):
        if not self.exists(label):
            self.set.add(ForemostNode(label, graph, time))
        return self.get(label)


    def subset(self, alist):
        subset = ForemostNodes()
        for node in alist:
            subset.set.add(node)
        return subset
