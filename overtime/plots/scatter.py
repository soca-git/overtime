
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
        parent : Node/Edge
            A valid Node or Edge object.
        index : Integer
            The index of the node on the plot.
        x : Float
            The x coordinate of the node.
        y : Float
            The y coordinate of the node.
        
        Object Propertie(s):
        --------------------
        parent : Node/Edge
            The corresponding parent object in the graph.
        index : Integer
            The index of the node on the plot.
        x : Float
            The x coordinate of the node.
        y : Float
            The y coordinate of the node.

        See also:
        ---------
            Scatter
    """

    def __init__(self, index, x=None, y=None, parent=None):
        self.parent = parent
        self.index = index
        self.x = index if x is None else x
        self.y = random.uniform(0, 1) if y is None else y


class Scatter():
    class_name = 'scatter'
    """
        A scatter plot.

        Class Propertie(s):
        -------------------
        class_name : String
            The name of the class, used for labelling.

        See also:
        ---------
            Plot
            Circle
            Slice
    """

    def __init__(self, graph, x=None, y=None):
        self.graph = graph
        self.x = x
        self.y = y
        self.figure, self.axis = plt.subplots(1)
        self.points = []


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



class NodeScatter(Scatter):
    """
        A scatter plot for graph nodes.

        Class Propertie(s):
        -------------------
        class_name : String
            The name of the class, used for labelling.

        See also:
        ---------
            Plot
            Circle
            Slice
    """
    class_name = 'node_scatter'

    def __init__(self, graph, x=None, y=None, bubble_metric=None):
        super().__init__(graph, x, y)
        self.bubble_metric = bubble_metric
        self.create()
        self.draw()
        self.cleanup()
        self.show()


    def create(self):
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
        self.draw_points()
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

        i = 0
        for node in self.graph.nodes.set:
            if self.bubble_metric:
                label = node.label + '\n' + str(node.data[self.bubble_metric])
            else:
                label = node.label

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
            A method of NodeScatter.

            Returns:
            --------
                None, cleans up plot axis.
        """
        self.axis.set_xticks([])
        self.axis.set_yticks([])
        self.axis.set_xticklabels([])
        self.axis.set_yticklabels([])


    def show(self):
        """
            A method of NodeScatter.

            Returns:
            --------
                None, shows figure.
        """
        _ = self.figure.show()
