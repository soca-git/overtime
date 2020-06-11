
from inputs.classes import CSVInput

from components.nodes import Nodes, Node

network_csv = CSVInput('network', 'csv', './network.csv')
network_csv.print()
network_csv.read()

nodes = Nodes()
for i, tedge in network_csv.data.items():
        nodes.add(Node(tedge['source']))
        nodes.add(Node(tedge['sink']))

print(nodes.labels)
for node in nodes.set:
    print(node, node.label)

for label in nodes.labels:
    print(label)
