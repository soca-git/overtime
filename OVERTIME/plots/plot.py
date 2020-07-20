
import matplotlib.pyplot as plt

class Plot:
    """
        Base Plot class.
    """

    def __init__(self, graph, axes, time=None):
        self.graph = graph
        self.time = str(time)[0]
        self.nodes = {}
        self.edges = {}
        self.axes = axes
        self.create()
        self.draw()


    def create(self):
        self.create_nodes()
        self.create_edges()


    def draw(self):
        if self.time is not None:
            self.draw_figure()
        self.draw_nodes()
        self.draw_edges()
        self.cleanup()


    def create_nodes(self):
        pass


    def create_edges(self):
        pass


    def draw_figure(self):
        title = 'time ' + self.time
        self.axes.set_title(
            label=title,
            loc='center'
        )

    
    def draw_nodes(self):
        pass


    def draw_edges(self):
        pass


    def cleanup(self):
        pass
