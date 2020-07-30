
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from components.digraphs import TemporalDiGraph


input_data = CSVInput('./network.csv')
graph = TemporalGraph('TestNetwork1')
graph.build(input_data)

digraph = TemporalDiGraph('TestNetwork2')
digraph.build(input_data)

graph.details()
graph.print()

digraph.details()
digraph.print()
