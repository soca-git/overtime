
import matplotlib.pyplot as plt
import imageio

from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from algorithms.foremost import CalculateForemostTree
from plots.circle import Circle



graph = TemporalGraph('TestNetwork', data=CSVInput('./network.csv'))
labels = []
for t in graph.edges.timespan():
    figure, axes = plt.subplots(1)
    labels.append('examples/time_' + str(t) + '.png')
    Circle(graph.get_snapshot(t), axes, 'TestNetwork', time=t)
    figure.savefig(labels[-1], format='png')

images = [imageio.imread(f) for f in labels]
imageio.mimsave('examples/network.gif', images, duration=2)

input("Press enter key to exit...")
