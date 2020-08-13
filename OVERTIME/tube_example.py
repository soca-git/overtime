
from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from plots.plotter import Plotter
from plots.circle import Circle
from plots.slice import Slice
from algorithms.foremost import CalculateForemostTree


tube = TemporalDiGraph('TubeNetwork', data=CSVInput('./tube.csv'))
tube.details()

plotter = Plotter()
# plotter.single(Circle, tube.get_graph_by_interval((840, 860)), ordered=True, save=True)
# plotter.single(Circle, CalculateForemostTree(tube.get_graph_by_interval((840, 860)), 'Blackhorse Road'), ordered=True, save=True)
# plotter.single(Slice, CalculateForemostTree(tube.get_graph_by_interval((840, 860)), 'Blackhorse Road'), slider=True, save=True)
plotter.single(Circle, CalculateForemostTree(tube.get_graph_by_interval((850, 920)), 'Warren Street'), ordered=True, save=True)
# plotter.single(Circle, tube, save=True)
plotter.single(Slice, tube, save=False)

input("Press enter key to exit...")
