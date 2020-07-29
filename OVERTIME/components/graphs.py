
from components.nodes import Nodes
from components.edges import Edges, TemporalEdges



class Graph:
    """
        A class which represents a graph consisting of nodes & edges.
    """

    def __init__(self, label, build=False, data=None):
        self.label = label
        self.directed = False
        self.nodes = Nodes()
        self.edges = Edges()

        if build:
            self.build(data)
        

    def build(self, data):
        for i, edge in data.data.items():
            self.edges.add(edge['node1'], edge['node2'], self.nodes)


    def details(self):
        print("\n\tGraph Details: \n\tLabel: %s \n\tDirected: %s" %(self.label, self.directed))
        print("\t#Nodes: %s \n\t#Edges: %s \n" % (self.nodes.count(), self.edges.count()))



class TemporalGraph(Graph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, build=False, data=None):
        super().__init__(label)
        self.edges = TemporalEdges()

        if build:
            self.build(data)


    def build(self, data):
        for i, edge in data.data['edges'].items():
            self.edges.add(edge['node1'], edge['node2'], self.nodes, edge['time'])


    def get_graph_by_time(self, time):
        label = self.label + ' [time: ' + str(time) + ']'
        graph = TemporalGraph(label)
        graph.edges = self.edges.get_edge_by_time(time)
        graph.nodes = self.nodes
        return graph


    def get_graph_by_interval(self, interval):
        label = self.label + ' [time: ' + str(interval) + ']'
        graph = TemporalGraph(label)
        graph.edges = self.edges.get_edge_by_interval(interval)
        graph.nodes = self.nodes
        return graph


    def print(self):
        self.nodes.print()
        print()
        self.edges.print()
        print()
