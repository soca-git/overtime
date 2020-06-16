
from inputs.classes import CSVInput
from components.graphs import TemporalGraph

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)


print("%5s %s" % (" ", " ".join(graph.edges.get_labels())) )
for i in range(1,11):
    row = [0]*8
    active = graph.edges.get_edge_by_time(i).get_labels()
    for label in active:
        index = graph.edges.get_labels().index(label)
        row[index] = 1
    print("%3s | %2s" % (i, "  ".join(map(str, row))) )
