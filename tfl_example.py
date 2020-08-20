
import overtime as ot
import pandas as pd

network = ot.TemporalDiGraph('TflNetwork', data=ot.CsvInput('./bakerloo-outbound.csv'))
network.details()
network.edges.timespan()

stations_df = pd.read_csv('bakerloo-stations.csv')
network.nodes.add_data(stations_df)

plotter = ot.Plotter()
plotter.single(ot.Slice, network)

# brix = network.get_node_connections('Brixton')
# plotter.single(ot.Slice, brix)
# oxcirc = network.get_node_connections('Oxford Circus')
# plotter.single(ot.Slice, oxcirc)
# plotter.single(ot.Slice, oxcirc.get_graph_by_interval((890, 910)))
# plotter.single(ot.Circle, oxcirc.get_graph_by_interval((890, 910)))

# brix_tree = ot.calculate_foremost_tree(network.get_graph_by_interval((890,910)), 'Brixton')
# plotter.single(ot.Circle, brix_tree)
# plotter.single(ot.Slice, brix_tree)

# oxcirc_tree = ot.calculate_foremost_tree(network.get_graph_by_interval((880,910)), 'Oxford Circus')
# plotter.single(ot.Circle, oxcirc_tree)

input("Press enter key to exit...")
