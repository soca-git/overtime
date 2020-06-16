
from inputs.classes import CSVInput
from components.nodes import Nodes
from components.edges import TemporalEdges

network_csv = CSVInput('network', 'csv', './network.csv')
network_csv.print()
network_csv.read()

nodes = Nodes()

edges = TemporalEdges()
for i, edge in network_csv.data.items():
    edges.add(edge['source'], edge['sink'], nodes, edge['time'])
