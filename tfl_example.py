
import overtime as ot

network = ot.TemporalDiGraph('TubeNetwork', data=ot.CsvInput('./victoria-outbound.csv'))
network.details()
network.edges.timespan()

plotter = ot.Plotter()
plotter.single(ot.Circle, network)
plotter.multi(ot.Circle, [
    network.get_snapshot(840),
    network.get_snapshot(841),
    network.get_snapshot(842),
    network.get_snapshot(843),
    network.get_snapshot(844),
    ]
)
#plotter.single(ot.Slice, network)


input("Press enter key to exit...")
