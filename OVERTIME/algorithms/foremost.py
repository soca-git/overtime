
from components.trees import ForemostTree



def CalculateForemostTree(graph, root):
    """
        A method which returns the foremost tree for a specified root.
    """
    if not graph.nodes.exists(root):
        print('Error: ' + root + ' does not exist in this graph.')
        return None

    timespan = graph.edges.timespan()
    start = timespan[0]
    end = timespan[-1]

    tree = ForemostTree(graph.label, root, start)

    for node in graph.nodes.set:
        tree.nodes.add(node.label, tree)

    root = tree.root
    root.start = start

    for edge in graph.edges.set:
        departure = tree.nodes.get(edge.source.label)
        destination = tree.nodes.get(edge.sink.label)
        if edge.end <= end and edge.start >= departure.time:
            if edge.end < destination.time:
                tree.edges.add(edge.source.label, edge.sink.label, tree.nodes, edge.start, edge.end)
                destination.time = edge.end
        elif edge.start >=end:
            break

    return tree
