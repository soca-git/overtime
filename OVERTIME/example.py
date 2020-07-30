
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from components.digraphs import TemporalDiGraph



graph = TemporalGraph('TestNetwork1', data=CSVInput('./network.csv'))

digraph = TemporalDiGraph('TestNetwork2', data=CSVInput('./network.csv'))

graph.details()
graph.print()

digraph.details()
digraph.print()
