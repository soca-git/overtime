
from inputs.classes import CSVInput
from components.graphs import TemporalGraph
from components.digraphs import TemporalDiGraph
from plots.plotter import Plotter
from plots.circle import Circle


graph = TemporalGraph('TestNetwork1', data=CSVInput('./network.csv'))

digraph = TemporalDiGraph('TestNetwork2', data=CSVInput('./network.csv'))

graph.details()
graph.print()

digraph.details()
digraph.print()


myplotter = Plotter()
myplotter.single(Circle, graph)
myplotter.single(Circle, digraph)

myplotter.multi(
    Circle,
    [graph.get_graph_by_time(6), graph.get_graph_by_time(7)]
)


snapshots = []
for t in graph.edges.timespan():
    snapshots.append(graph.get_graph_by_time(t))

myplotter.multi(Circle, snapshots)
