
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree

from plots.plotter import Plotter
from plots.circle import Circle


input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork')
graph.build_from_csv(input_data)

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
        CalculateForemostTree(graph, 'a').tree,
        CalculateForemostTree(graph, 'b').tree,
        CalculateForemostTree(graph, 'c').tree,
        CalculateForemostTree(graph, 'd').tree,
        CalculateForemostTree(graph, 'e').tree
    ]
)

myplotter.single(Circle, CalculateForemostTree(graph.get_graph_by_interval(range(0,7)), 'a').tree)

input("Press enter key to exit...")
