
from components.trees import ForemostTree



class CalculateForemostTree:
    """
        A class which represents the foremost path algorithm.
    """

    def __init__(self, graph, root):
        self.graph = graph
        timespan = self.graph.edges.timespan()
        start = timespan[0]
        end = timespan[-1]+1
        self.tree = ForemostTree(graph.label, root, start)
        self.calculate(root, start, end)


    def calculate(self, root, start, end):
        tree = self.tree
        for node in self.graph.nodes.set:
            tree.nodes.add(node.label)

        root = tree.root
        root.time = start

        for edge in self.graph.edges.stream:
            departure = tree.nodes.get(edge.source.label)
            destination = tree.nodes.get(edge.sink.label)
            if edge.time + edge.duration <= end and edge.time >= departure.time:
                if edge.time + edge.duration < destination.time:
                    self.tree.edges.add(edge.source.label, edge.sink.label, tree.nodes, edge.time, edge.duration)
                    destination.time = edge.time + edge.duration
            elif edge.time >=end:
                break
