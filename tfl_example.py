
import overtime as ot
import pandas as pd

network = ot.TemporalDiGraph('TflNetwork', data=ot.CsvInput('./bakerloo_piccadilly-inbound_outbound.csv'))
network.details()
network.edges.timespan()

stations_df = pd.read_csv('bakerloo_piccadilly-stations.csv')
network.nodes.add_data(stations_df)

# plotter = ot.Plotter()
# plotter.single(ot.Slice, network)

# pcircus = network.get_node_connections('Piccadilly Circus')
# plotter.single(ot.Circle, pcircus)
# plotter.single(ot.Slice, pcircus)
# gpark = network.get_node_connections('Green Park')
# ot.Circle(gpark)
# ot.Slice(gpark)

# pcircus_tree = ot.calculate_foremost_tree(network, 'Piccadilly Circus')
# ot.Circle(pcircus_tree)
# ot.Slice(pcircus_tree)

# gpark_tree = ot.calculate_foremost_tree(network, 'Green Park')
# ot.Circle(gpark_tree)
# ot.Slice(gpark_tree)

sub_network = network.get_graph_by_interval((850, 880))
sub_network.nodes.add_data(stations_df)
for node in sub_network.nodes.set:
    node.data['reachability'] = ot.calculate_reachability(sub_network, node.label)

ot.NodeScatter(sub_network, y='reachability', bubble_metric='reachability')
ot.NodeScatter(sub_network, x='lon', y='lat', bubble_metric='reachability')
ot.Slice(sub_network)
ot.Circle(sub_network)

pcircus_tree = ot.calculate_foremost_tree(sub_network, 'Piccadilly Circus')
pcircus_tree.nodes.add_data(stations_df)
ot.Circle(pcircus_tree)
ot.Slice(pcircus_tree)
ot.NodeScatter(pcircus_tree, x='lon', y='lat', bubble_metric='foremost_time')


input("Press enter key to exit...")
