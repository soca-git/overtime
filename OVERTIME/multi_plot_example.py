
import matplotlib.pyplot as plt

from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from plots.circle import Circle

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)
graph.print()

graph.edges.add('b', 'e', graph.nodes, 4)


figure, axes = plt.subplots(nrows=3, ncols=3)
#times = graph.edges.active_times()
times = range(0, 10)
i = 0
for row in axes:
    for col in row:
        Circle(graph.get_graph_by_time(times[i]), col, times[i])
        i += 1
        if i > 9:
            break

plt.tight_layout(pad=0.1)
figure.set_size_inches(14, 10)
figure.savefig('examples/multiplot.png', format='png')
figure.show()

input("Press enter key to exit...")
