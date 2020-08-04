
from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from algorithms.foremost import CalculateForemostTree

from plots.plotter import Plotter
from plots.circle import Circle


graph = TemporalDiGraph('TestNetwork', data=CSVInput('./network.csv'))

myplotter = Plotter()
myplotter.single(Circle, graph)

myplotter.single(Circle, graph.get_snapshot(7))
myplotter.multi(Circle, [graph.get_snapshot(4), graph.get_snapshot(7)])

myplotter.multi(Circle,
    [
        graph.get_graph_by_interval((0, 7)),
        graph.get_graph_by_interval((7, 14))
    ]
)

myplotter.multi(
    Circle,
    [
        CalculateForemostTree(graph, 'a'),
        CalculateForemostTree(graph, 'b'),
        CalculateForemostTree(graph, 'c'),
        CalculateForemostTree(graph, 'd'),
        CalculateForemostTree(graph, 'e')
    ]
)

myplotter.single(Circle, CalculateForemostTree(graph.get_graph_by_interval((0,7)), 'a'))

input("Press enter key to exit...")
