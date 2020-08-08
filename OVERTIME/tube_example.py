
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
plotter.single(Slice, tube, save=True, slider=True)

# plotter.single(Circle, CalculateForemostTree(tube, 'Holborn'))
# plotter.single(Slice, CalculateForemostTree(tube, 'Holborn'))


input("Press enter key to exit...")
