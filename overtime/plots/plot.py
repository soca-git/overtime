
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap



class Plot:
    """
        Base plot class.

        Class Propertie(s):
        -------------------
        class_name : String
            The name of the class, used for labelling.

        Parameter(s):
        -------------
        graph : Graph
            A valid Graph class/subclass.
        figure : Figure
            A pyplot figure object.
        axis : axis
            A pyplot axis object.
        title : String
            A custom title for the plot.
        ordered : Boolean
            If the Plot class supports the ordering of a plot in some useful way, enable it.
        slider : Boolean
            If the Plot class supports sliders, enable it.
        show : Boolean
            Show the plot (can be overridden).

        Object Propertie(s):
        --------------------
        name : String
            Name of the plot, used for labelling.
        graph : Graph
            The corresponding graph object to be plotted.
        title : String
            A custom title for the plot. One is automatically generated otherwise.
        nodes : List
            A list of the plot's node objects.
        edges : List
            A list of the plot's edge objects.
        labels : List
            A list of the plot's labels.
        figure : Figure
            A pyplot figure object.
        axis : axis
            A pyplot axis object.
        is_ordered : Boolean
            Whether or not the plot was ordered during creation.
        has_slider : Boolean
            Whether or not the resulting figure includes sliders for navigation.
        show : Boolean
            Whether or not the figure is to be shown by the plotter after creation is complete.

        See also:
        ---------
            Circle
            Slice
    """
    class_name = 'plot'

    def __init__(self, graph, figure, axis, title=None, ordered=True, slider=False, show=True):
        self.name = ''
        self.graph = graph
        self.title = title
        self.nodes = []
        self.edges = []
        self.labels = []
        self.figure = figure
        self.axis = axis
        self.is_ordered = ordered
        self.has_slider = slider
        self.show = show
        self.update_name()
        self.create()
        self.draw()


    def update_name(self):
        name = self.class_name + '-' + self.graph.label
        self.name = name.replace(' ', '_').replace(':','').replace(',','')


    def create(self):
        self.create_nodes()
        self.create_edges()


    def draw(self):
        if self.title is not None:
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
        if not self.graph.static:
            title = title + ' [time: ' + str(self.graph.edges.start()) + ']'

        self.axis.set_title(
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
