from inputs.classes import CSVInput
from components.graphs import TemporalGraph

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork')
graph.build(input_data)


# calculate foremost time (to be added)
foremost = {}
a = graph.nodes.get('a')
start = graph.edges.firsttime()
end = graph.edges.lifetime()

for node in graph.nodes.set:
    foremost[node.label] = {}
    foremost[node.label]['time'] = float('inf')
    foremost[node.label]['source'] = ''

foremost[a.label]['time'] = start
foremost[a.label]['source'] = a.label

for edge in graph.edges.set:
    if edge.time + edge.duration <=end and edge.time >= foremost[edge.source.label]['time']:
        if edge.time + edge.duration < foremost[edge.sink.label]['time']:
            foremost[edge.sink.label]['time'] = edge.time + edge.duration
            foremost[edge.sink.label]['source'] = edge.source.label
    elif edge.time >= end:
        break

for node, info in foremost.items():
    print("{} | {},{}".format(node, info['time'], info['source']))
