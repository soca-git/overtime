
import matplotlib.pyplot as plt

from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree
from plots.circle import Circle

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork')
graph.build_from_csv(input_data)
graph.print()

figure, axes = plt.subplots(1)
Circle(graph, axes, 'TestNetwork')

plt.tight_layout(pad=0.1)
figure.set_size_inches(14, 10)
figure.savefig('examples/graph.png', format='png')

figure, axes = plt.subplots(nrows=2, ncols=2)
foremost_a = CalculateForemostTree(graph, 'a')
Circle(foremost_a.tree, axes[0][0], 'root: a')

foremost_b = CalculateForemostTree(graph, 'b')
Circle(foremost_b.tree, axes[0][1], 'root: b')

foremost_c = CalculateForemostTree(graph, 'c')
Circle(foremost_c.tree, axes[1][0], 'root: c')

foremost_d = CalculateForemostTree(graph, 'd')
Circle(foremost_d.tree, axes[1][1], 'root: d')

plt.tight_layout(pad=0.1)
figure.set_size_inches(14, 10)
figure.savefig('examples/foremost_trees.png', format='png')

plt.show()

input("Press enter key to exit...")
