
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from components.digraphs import TemporalDiGraph


input_data = CSVInput('network', 'csv', './network.csv')
graph = TemporalGraph('TestNetwork1')
graph.build_from_csv(input_data)

digraph = TemporalDiGraph('TestNetwork2')
digraph.build_from_csv(input_data)

graph.details()
graph.print()

digraph.details()
digraph.print()
