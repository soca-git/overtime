
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree
from plots.circle import Circle

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)
graph.print()

myplot = Circle(graph)
myplot.display()

foremost_a = CalculateForemostTree(graph, 'a')
myplot = Circle(foremost_a.tree)
myplot.display()

foremost_c = CalculateForemostTree(graph, 'c')
myplot = Circle(foremost_c.tree)
myplot.display()

input("Press enter key to exit...")
