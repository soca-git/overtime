
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)
graph.print()

foremost_a = CalculateForemostTree(graph, 'a')
foremost_b = CalculateForemostTree(graph, 'b')
foremost_c = CalculateForemostTree(graph, 'c')
foremost_d = CalculateForemostTree(graph, 'd')
foremost_e = CalculateForemostTree(graph, 'e')

foremost_a.tree.print()
foremost_b.tree.print()
foremost_d.tree.print()
