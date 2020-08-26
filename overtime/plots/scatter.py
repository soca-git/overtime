
import math, random
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from overtime.plots.plot import Plot


class ScatterPoint():
    """
        A class to represent a node on a scatter plot.

        Parameter(s):
        -------------
        index : Integer
            The index of the node on the plot.
        x : Float
            The x coordinate of the node.
        y : Float
            The y coordinate of the node.
        parent : Node/Edge
            A valid Node or Edge object.
        
        Object Propertie(s):
        --------------------
        index : Integer
            The index of the node on the plot.
        x : Float
            The x coordinate of the node.
        y : Float
            The y coordinate of the node.
        parent : Node/Edge
            The corresponding Node or Edge object in the graph.

        See also:
        ---------
            NodeScatter
    """

    def __init__(self, index, x=None, y=None, parent=None):
        self.index = index
        self.x = index if x is None else x
        self.y = random.uniform(0, 1) if y is None else y
        self.parent = parent



class NodeScatter(Plot):
    """
        A scatter plot for graph nodes.

        Class Propertie(s):
        -------------------
        class_name : String
            The name of the class, used for labelling.

        Parameter(s):
        -------------
        graph : Graph
            A valid Graph class/subclass.
        x : String
            The x-axis metric to be used when plotting the nodes.
            Must correspond to a data key of the node objects.
        y : String
            The y-axis metric to be used when plotting the nodes.
            Must correspond to a data key of the node objects.
        bubble_metric : String
            The bubble metric to be used when plotting the nodes.
            Must correspond to a data key of the node objects.
        title : String
            A custom title for the plot.

        Object Propertie(s):
        --------------------
        graph : Graph
            The corresponding graph object to be plotted.
        x : String
            The x-axis metric to be used to plot nodes.
        y : String
            The y-axis metric to be used to plot nodes.
        bubble_metric : String
            The bubble metric to be used when plotting the nodes.
        title : String
            A custom title for the plot. One is automatically generated otherwise.
        figure : Figure
            A pyplot figure object.
        axis : Axis
            A pyplot axis object.
        points : List
            A list of ScatterPoint objects.

        See also:
        ---------
            ScatterPoint
            Plot
    """
    class_name = 'node_scatter'

    def __init__(self, graph, x=None, y=None, bubble_metric=None, title=None):
        self.graph = graph
        self.x = x
        self.y = y
        self.bubble_metric = bubble_metric
        self.title = title if title else graph.label
        self.figure, self.axis = plt.subplots(1)
        self.points = []
        # build plot.
        self.create()
        self.draw()
        self.cleanup()
        self.figure.show()


    def create(self):
        """
            A method of NodeScatter.

            Returns:
            --------
                None, creates plot objects.
        """
        self.create_points()


    def create_points(self):
        """
            A method of NodeScatter.

            Returns:
            --------
                None, creates ScatterPoint objects.
        """
        i = 0
        x,y = None,None
        # for each node.
        for node in self.graph.nodes.set:
            # if a metric was specified for x.
            if self.x:
                x = node.data[self.x] # update x.
            # if a metric was specified for y.
            if self.y:
                y = node.data[self.y] # update y.
            # create a scatter point object for the node.            
            self.points.append(ScatterPoint(i, x, y, parent=node))
            i += 1


    def draw(self):
        """
            A method of NodeScatter.

            Returns:
            --------
                None, draws the plot.
        """
        self.draw_points()
        self.draw_title()
        self.axis.set_facecolor('slategrey')
        self.figure.set_size_inches(28, 20)
        plt.draw()


    def draw_points(self):
        """
            A method of NodeScatter.

            Returns:
            --------
                None, draws the points of the plot.
        """
        n = self.graph.nodes.count() # number of nodes in the graph.
        pos = {}
        pos['x'] = [point.x for point in self.points] # x coordinates of every node.
        pos['y'] = [point.y for point in self.points] # y coordinates of every node.
        
        cmap = self.set3colormap(n) # color map with enough colors for n nodes.
        if self.bubble_metric:
            # consolidate specified metric node data into a list (absolute values).
            node_metrics = [abs(node.data[self.bubble_metric]) for node in self.graph.nodes.set]
            max_m = max([0 if x == float('inf') else x for x in node_metrics]) # get the metrics list maximum.
            # create a normalized list of metrics.
            normalized_metrics = [m/max_m for m in node_metrics]
            bmet = [m*1000 for m in normalized_metrics] # size scatter points based on normalized bubble metric.
            colors = bmet # color nodes based on bubble metric.
        else:
            colors = [x for x in range(0, n)] # colors index for every node.
            bmet = 1000 # default node size.

        # draw the nodes using pyplot scatter ().
        self.axis.scatter(
            pos['x'], pos['y'], s=bmet, c=colors, cmap=cmap, alpha=0.5, zorder=1
        )

        # draw the node labels.
        i = 0
        # for each node in the graph.
        for node in self.graph.nodes.set:
            # if a bubble metric was provided.
            if self.bubble_metric:
                # add bubble metric to the label.
                label = node.label + '\n' + str(node.data[self.bubble_metric])
            else:
                label = node.label # default label
            # add the label text.
            self.axis.text(
                pos['x'][i], pos['y'][i],
                label,
                color='white',
                ha='center', va='center',
                fontsize='small'
            )
            i += 1


    def cleanup(self):
        """
            A method of Plot/NodeScatter.

            Returns:
            --------
                None, updates figure & axis properties & styling.
        """
        self.remove_xticks(self.axis)
        self.remove_yticks(self.axis)
        self.style_axis(self.axis)
        self.axis.margins(0.1, 0.1) # update plot margins.
