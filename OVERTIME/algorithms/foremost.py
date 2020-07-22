
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
        tree.nodes.add(node.label)

    root = tree.root
    root.time = start

    for edge in graph.edges.stream:
        departure = tree.nodes.get(edge.source.label)
        destination = tree.nodes.get(edge.sink.label)
        if edge.time + edge.duration <= end and edge.time >= departure.time:
            if edge.time + edge.duration < destination.time:
                tree.edges.add(edge.source.label, edge.sink.label, tree.nodes, edge.time, edge.duration)
                destination.time = edge.time + edge.duration
        elif edge.time >=end:
            break

    return tree
