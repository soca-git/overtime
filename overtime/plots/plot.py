
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
        """
            A method of Plot.

            Returns:
            --------
                None, combines the graph label and plot class name
                and updates self.name for the plot.
        """
        name = self.class_name + '-' + self.graph.label
        # replace is used to filter characters that are not supported in file names.
        self.name = name.replace(' ', '_').replace(':','').replace(',','')


    def create(self):
        """
            A method of Plot.

            Returns:
            --------
                None, creates plot's nodes & edges.
        """
        self.create_nodes() # create the plot's nodes.
        self.create_edges() # create the plot's edges.


    def create_nodes(self):
        """
            A method of Plot.
                Base method to be customized for each Plot subclass.
                Creates plot's nodes.
        """
        pass


    def create_edges(self):
        """
            A method of Plot.
                Base method to be customized for each Plot subclass.
                Creates plot's edges.
        """
        pass


    def draw(self):
        """
            A method of Plot.

            Returns:
            --------
                None, draws plot's title, nodes & edges and cleans up figure & axis.
        """
        if self.title is not None:
            self.draw_title() # draw title.
        self.draw_nodes() # draw the plot's nodes.
        self.draw_edges() # draw the plot's edges.
        self.cleanup() # cleanup the figure & axis.


    def draw_title(self):
        """
            A method of Plot.

            Returns:
            --------
                None, draws plot title.
        """
        title = '' if self.title is None else self.title
        # if the graph is temporal.
        if not self.graph.static:
            # add the graph timespan to the plot title.
            title = title + ' [time: ' + str(self.graph.edges.timespan()) + ']'
        # draw the title.
        self.axis.set_title(
            label=title,
            loc='center'
        )

    
    def draw_nodes(self):
        """
            A method of Plot.
                Base method to be customized for each Plot subclass.
                Draws plot's nodes.
        """
        pass


    def draw_edges(self):
        """
            A method of Plot.
                Base method to be customized for each Plot subclass.
                Draws plot's edges.
        """
        pass


    def cleanup(self):
        """
            A method of Plot.
                Base method to be customized for each Plot subclass.
                Cleans up figure & axis.
        """
        pass


    def set3colormap(self, n):
        """
            A method of Plot.
            Parameter(s):
            -------------
            n : Integer
                Number of objects to be assigned a color.
            
            Returns:
            --------
            cmap : ListedColorMap
                A pyplot ListedColorMap object.
                Map has enough colors to assign to n objects without color adjacency.
        """
        n = math.ceil(n/12) # Set3 cmap has 12 colours, divide n and ceil.
        cmap = cm.get_cmap('Set3')
        # Return an expanded Set3 cmap with enough repeating colors
        # to cover the number of objects to be drawn
        return ListedColormap(cmap.colors*n)
