
from generators.nx_random import RandomGNP
from components.graphs import TemporalGraph
from plots.plotter import Plotter
from plots.circle import Circle

data0 = RandomGNP()
graph0 = TemporalGraph('TestNetwork [p=0.5]', data=data0)

data1 = RandomGNP(n=10, p=0.1)
graph1 = TemporalGraph('TestNetwork [p=0.1]', data=data1)

myplotter = Plotter()
myplotter.multi(Circle, [graph0.get_graph_by_time(0), graph1.get_graph_by_time(0)])

myplotter.multi(
    Circle,
    [
        graph1.get_graph_by_time(0),
        graph1.get_graph_by_time(1),
        graph1.get_graph_by_time(2),
        graph1.get_graph_by_time(3),
        graph1.get_graph_by_time(4),
        graph1.get_graph_by_time(5),
        graph1.get_graph_by_time(6),
        graph1.get_graph_by_time(7),
        graph1.get_graph_by_time(8),
        graph1.get_graph_by_time(9),
        graph1.get_graph_by_time(10),
    ]
)

input("Press enter key to exit...")
