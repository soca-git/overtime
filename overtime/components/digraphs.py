
from overtime.components.graphs import Graph, TemporalGraph
from overtime.components.nodes import Nodes
from overtime.components.arcs import Arcs, TemporalArcs



class DiGraph(Graph):
    """
        A class which represents a graph consisting of nodes & arcs.
    """

    def __init__(self, label, data=None):
        super().__init__(label)
        self.directed = True
        self.edges = Arcs(self)

        if data is not None:
            self.build(data)
        


class TemporalDiGraph(TemporalGraph):
    """
        A class which represents a temporal graph consisting of nodes & temporal arcs.
    """

    def __init__(self, label, data=None):
        super().__init__(label)
        self.directed = True
        self.edges = TemporalArcs(self)

        if data is not None:
            self.build(data)


    def get_snapshot(self, time):
        label = self.label + ' [time: ' + str(time) + ']'
        graph = DiGraph(label)
        for edge in self.edges.get_active_edges(time).set:
            graph.add_edge(edge.node1.label, edge.node2.label)
        for node in self.nodes.set:
            graph.add_node(node.label)
        return graph


    def get_temporal_subgraph(self, interval):
        label = self.label + ' [time: ' + str(interval) + ']'
        graph = TemporalDiGraph(label)
        graph.edges = self.edges.get_edge_by_interval(interval)
        for node in self.nodes.set:
            graph.add_node(node.label)
        return graph
