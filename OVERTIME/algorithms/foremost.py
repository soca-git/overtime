
from components.trees import ForemostTree



def CalculateForemostTree(graph, root):
    """
        A method which returns the foremost tree for a specified root.
    """
    timespan = graph.edges.timespan()
    start = timespan[0]
    end = timespan[-1]+1
    tree = ForemostTree(graph.label, root, start)

    for node in graph.nodes.set:
        tree.nodes.add(node.label, tree)

    root = tree.root
    root.start = start

    for edge in graph.edges.set:
        departure = tree.nodes.get(edge.source.label)
        destination = tree.nodes.get(edge.sink.label)
        if edge.start + edge.duration <= end and edge.start >= departure.start:
            if edge.start + edge.duration < destination.start:
                tree.edges.add(edge.source.label, edge.sink.label, tree.nodes, edge.start, edge.duration)
                destination.start = edge.start + edge.duration
        elif edge.start >=end:
            break

    return tree
