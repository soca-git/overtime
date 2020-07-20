
import matplotlib.pyplot as plt
import imageio

from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree
from plots.circle import Circle

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)
graph.print()

figure, axes = plt.subplots(1)
Circle(graph, axes)

figure, axes = plt.subplots(nrows=2, ncols=2)
foremost_a = CalculateForemostTree(graph, 'a')
Circle(foremost_a.tree, axes[0][0])

foremost_c = CalculateForemostTree(graph, 'c')
Circle(foremost_c.tree, axes[0][1])

# labels = []
# for t in graph.edges.active_times():
#     figure, axes = plt.subplots(1)
#     labels.append('time_' + str(t) + '.png')
#     Circle(graph.get_graph_by_time(t), axes, t)
#     figure.savefig(labels[-1], format='png')

# images = [imageio.imread(f) for f in labels]
# imageio.mimsave('network.gif', images, duration=3)

plt.show()

input("Press enter key to exit...")
