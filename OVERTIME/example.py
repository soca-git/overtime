
import matplotlib.pyplot as plot
import imageio

from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree
from plots.circle import Circle

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)
graph.print()

# myplot = Circle(graph)
# myplot.display()

# foremost_a = CalculateForemostTree(graph, 'a')
# myplot = Circle(foremost_a.tree)
# myplot.display()

# foremost_c = CalculateForemostTree(graph, 'c')
# myplot = Circle(foremost_c.tree)
# myplot.display()

labels = []
for t in graph.edges.active_times():
    labels.append('time_' + str(t) + '.png')
    Circle(graph.get_graph_by_time(t))
    plot.savefig(labels[-1], format='png')

images = [imageio.imread(f) for f in labels]
imageio.mimsave('network.gif', images, duration=3)

input("Press enter key to exit...")
