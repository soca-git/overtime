
from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from plots.plotter import Plotter
from plots.circle import Circle
from plots.slice import Slice
from algorithms.foremost import CalculateForemostTree


tube = TemporalDiGraph('TubeNetwork', data=CSVInput('./tube.csv'))
tube.details()

plotter = Plotter()
# plotter.single(Circle, tube, ordered=True)
# plotter.single(Slice, tube)

plotter.single(Circle, tube.get_graph_by_interval((840, 860)), ordered=True, save=True)
# plotter.single(Circle, CalculateForemostTree(tube.get_graph_by_interval((840, 860)), 'Blackhorse Road'), ordered=True)
# plotter.single(Slice, CalculateForemostTree(tube.get_graph_by_interval((840, 860)), 'Blackhorse Road'))

input("Press enter key to exit...")
