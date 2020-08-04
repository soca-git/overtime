
from components.nodes import Nodes
from components.edges import Edges, TemporalEdges



class Graph:
    """
        A class which represents a graph consisting of nodes & edges.
    """

    def __init__(self, label, data=None):
        self.label = label
        self.directed = False
        self.static = True
        self.nodes = Nodes()
        self.edges = Edges()

        if data is not None:
            self.build(data)
        

    def build(self, data):
        for i, edge in data.data.items():
            self.add_edge(edge['node1'], edge['node2'])


    def add_node(self, label):
        self.nodes.add(label, self)


    def add_edge(self, node1, node2):
        self.edges.add(node1, node2, self.nodes, self)


    def details(self):
        print("\n\tGraph Details: \n\tLabel: %s \n\tDirected: %s \n\tStatic: %s" %(self.label, self.directed, self.static))
        print("\t#Nodes: %s \n\t#Edges: %s \n" % (self.nodes.count(), self.edges.count()))


    def print(self):
        self.nodes.print()
        print()
        self.edges.print()
        print()



class TemporalGraph(Graph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, data=None):
        super().__init__(label)
        self.static = False
        self.edges = TemporalEdges()

        if data is not None:
            self.build(data)


    def build(self, data):
        for i, edge in data.data['edges'].items():
            self.add_edge(edge['node1'], edge['node2'], edge['tstart'], edge['tend'])


    def add_edge(self, node1, node2, tstart, tend=None):
        self.edges.add(node1, node2, self.nodes, self, tstart, tend)


    def get_snapshot(self, time):
        label = self.label + ' [time: ' + str(time) + ']'
        graph = Graph(label)
        for edge in self.edges.get_active_edges(time).set:
            graph.add_edge(edge.node1.label, edge.node2.label)
        graph.nodes = self.nodes
        return graph


    def get_graph_by_interval(self, interval):
        label = self.label + ' [time: ' + str(interval) + ']'
        graph = TemporalGraph(label)
        graph.edges = self.edges.get_edge_by_interval(interval)
        graph.nodes = self.nodes
        return graph
