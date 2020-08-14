
from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from algorithms.reachability import CalculateNodeReachability


tube = TemporalDiGraph('TubeNetwork', data=CSVInput('./tube.csv'))
tube.details()

for node in tube.nodes.set:
    r = CalculateNodeReachability(tube.get_graph_by_interval((850, 920)), node.label)
    print(node.label, str(r))


input("Press enter key to exit...")
