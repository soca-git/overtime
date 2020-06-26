
from inputs.classes import CSVInput
from components.graphs import TemporalGraph

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)



# calculate foremost time (to be added)
foremost = {}
d = graph.nodes.get('d')
start = graph.edges.firsttime()
end = graph.edges.lifetime()

for node in graph.nodes.set:
    foremost[node.label] = {}
    foremost[node.label]['time'] = float('inf')
    foremost[node.label]['source'] = ''

foremost[d.label]['time'] = start
foremost[d.label]['source'] = d.label

for edge in graph.edges.stream:
    if edge.time + edge.duration and edge.time >= foremost[edge.source.label]['time']:
        if edge.time + edge.duration < foremost[edge.sink.label]['time']:
            foremost[edge.sink.label]['time'] = edge.time + edge.duration
            foremost[edge.sink.label]['source'] = edge.source.label
    elif edge.time >= end:
        break

for node, info in foremost.items():
    print("{} | {},{}".format(node, info['time'], info['source']))
