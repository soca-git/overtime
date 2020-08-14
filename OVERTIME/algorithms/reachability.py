
from algorithms.foremost import CalculateForemostTree



def CalculateNodeReachability(graph, root):
    """
        A method which returns the reachability (number) of a root in the graph.
    """
    if not graph.nodes.exists(root):
        print('Error: ' + str(root) + ' does not exist in this graph.')
        return None

    tree = CalculateForemostTree(graph, root)
    return tree.nodes.get_reachable().count()
