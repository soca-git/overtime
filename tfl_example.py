
import overtime as ot

network = ot.TemporalDiGraph('TubeNetwork', data=ot.CsvInput('./victoria-outbound.csv'))
network.details()

plotter = ot.Plotter()
plotter.single(ot.Slice, network)
