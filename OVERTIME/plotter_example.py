
from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from algorithms.foremost import CalculateForemostTree

from plots.plotter import Plotter
from plots.circle import Circle


graph = TemporalDiGraph('TestNetwork', data=CSVInput('./network.csv'))

myplotter = Plotter()
myplotter.single(Circle, graph)

myplotter.single(Circle, graph.get_graph_by_time(7))
myplotter.multi(Circle, [graph.get_graph_by_time(4), graph.get_graph_by_time(7)])

myplotter.multi(Circle,
    [
        graph.get_graph_by_interval(range(0, 7)),
        graph.get_graph_by_interval(range(7, 14))
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

myplotter.single(Circle, CalculateForemostTree(graph.get_graph_by_interval(range(0,7)), 'a'))

input("Press enter key to exit...")
