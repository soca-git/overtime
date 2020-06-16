
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

        if input_data.type == 'csv':
            self.build_from_csv(input_data)

        self.details()


    def build_from_csv(self, input_data):
        print("Building...")
        for i, edge in input_data.data.items():
            self.edges.add(edge['source'], edge['sink'], self.nodes)


    def details(self):
        print("\n\tGraph Details: \n\tLabel: %s" %(self.label))
        print("\t#Nodes: %s \n\t#Edges: %s \n" % (self.nodes.count(), self.edges.count()))



class TemporalGraph(Graph):
    """
        A class which represents a temporal graph consisting of nodes & temporal edges.
    """

    def __init__(self, label, input_data):
        self.label = label
        self.nodes = Nodes()
        self.edges = TemporalEdges()

        if input_data.type == 'csv':
            self.build_from_csv(input_data)

        self.details()


    def build_from_csv(self, input_data):
        for i, edge in input_data.data.items():
            self.edges.add(edge['source'], edge['sink'], self.nodes, edge['time'])

