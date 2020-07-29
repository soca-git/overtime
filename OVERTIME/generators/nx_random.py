
import networkx as nx
from generators.classes import Generator



class RandomGNP(Generator):
    """
        A GNP random graph with n edges where each edge is created with a possibility p.
    """

    def __init__(self, n=10, p=0.5, directed=False, start=0, end=10):
        super().__init__()
        self.generate(n, p, directed, start, end)


    def generate(self, n, p, directed, start, end):
        data = self.data
        ne, nn = 0, 0
        for t in range(start, end+1):
            static = nx.gnp_random_graph(n, p, directed=directed)
            for edge in static.edges:
                data['edges'][ne] = {}
                data['edges'][ne]['node1'] = edge[0]
                data['edges'][ne]['node2'] = edge[1]
                data['edges'][ne]['time'] = t
                ne += 1

            if t == start:
                for node in static.nodes:
                    data['nodes'][nn] = node
                    nn += 1
