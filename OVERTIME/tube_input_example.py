
from inputs.classes import TubeInput
from components.digraphs import TemporalDiGraph
from plots.plotter import Plotter
from plots.circle import Circle
from plots.slice import Slice
from algorithms.foremost import CalculateForemostTree


tube_input = TubeInput(['victoria', 'central'], ['1400'])
tube_input.print()


tube = TemporalDiGraph('TubeNetwork', data=tube_input)


plotter = Plotter()
plotter.single(Slice, tube, slider=False)
plotter.single(Circle, CalculateForemostTree(tube, 'Holborn'))

input("Press enter key to exit...")
