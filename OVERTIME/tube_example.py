
from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from plots.plotter import Plotter
from plots.circle import Circle
from plots.slice import Slice


tube = TemporalDiGraph('Tube Network', data=CSVInput('./tube.csv'))
tube.details()

plotter = Plotter()
plotter.single(Circle, tube, ordered=True)
plotter.single(Slice, tube, save=True)

snapshots = []
for t in tube.edges.timespan():
    snapshots.append(tube.get_snapshot(t))
plotter.multi(Circle, snapshots, save=True, ordered=True)

input("Press enter key to exit...")
