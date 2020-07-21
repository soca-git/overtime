
import matplotlib.pyplot as plt
import imageio

from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree
from plots.circle import Circle

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork')
graph.build_from_csv(input_data)
graph.print()

labels = []
for t in graph.edges.timespan():
    figure, axes = plt.subplots(1)
    labels.append('examples/time_' + str(t) + '.png')
    Circle(graph.get_graph_by_time(t), axes, 'TestNetwork', time=t)
    figure.savefig(labels[-1], format='png')

images = [imageio.imread(f) for f in labels]
imageio.mimsave('examples/network.gif', images, duration=2)

input("Press enter key to exit...")
