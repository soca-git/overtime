
from components.nodes import Nodes
from components.edges import Edges, TemporalEdges

class Graph:
    """
        A class which represents a graph consisting of nodes & edges.
    """

    def __init__(self, label, input_data):
        self.label = label
        self.nodes = Nodes()
        self.edges = Edges()

        print("Building graph...")
        if input_data.type == 'csv':
            self.build_from_csv(input_data)


    def build_from_csv(self, input_data):
        for i, edge in input_data.data.items():
            self.edges.add(edge['source'], edge['sink'], self.nodes)


    def details(self):
        print("\n\tGraph Details: \n\tLabel: %s" %(self.label))
        print("\t#Nodes: %s \n\t#Edges: %s \n" % (self.nodes.count(), self.edges.count()))



class TemporalGraph(Graph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, input_data=None):
        self.label = label
        self.nodes = Nodes()
        self.edges = TemporalEdges()

        print("Building graph...")
        if input_data is not None and input_data.type == 'csv':
            self.build_from_csv(input_data)


    def build_from_csv(self, input_data):
        for i, edge in input_data.data.items():
            self.edges.add(edge['source'], edge['sink'], self.nodes, edge['time'])


    def get_graph_by_time(self, time):
        graph = TemporalGraph('graph at time t=')
        graph.edges = self.edges.get_edge_by_time(time)
        graph.nodes = self.nodes
        return graph


    def print(self, start=None, end=None):
        self.nodes.print()
        self.edges.print(start, end)
