
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap



class Plot:
    """
        Base Plot class.
    """

    def __init__(self, graph, axes, title=None, time=None, ordered=True):
        self.graph = graph
        self.title = title
        self.time = time
        self.nodes = []
        self.edges = []
        self.labels = []
        self.axes = axes
        self.ordered = ordered
        self.create()
        self.draw()


    def create(self):
        self.create_nodes()
        self.create_edges()


    def draw(self):
        if self.title is not None or self.time is not None:
            self.draw_figure()
        self.draw_nodes()
        self.draw_edges()
        self.cleanup()


    def create_nodes(self):
        pass


    def create_edges(self):
        pass


    def draw_figure(self):
        title = '' if self.title is None else self.title
        if self.time is not None:
            title = title + ' [time: ' + str(self.time) + ']'

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


    def set3colormap(self, n):
        n = math.ceil(n/12)
        cmap = cm.get_cmap('Set3')
        return ListedColormap(cmap.colors*n)
