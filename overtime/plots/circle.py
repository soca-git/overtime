
import math
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from overtime.plots.plot import Plot
from overtime.plots.utils import vector_angle, bezier, circle_label_angle



class CircleNode():
    """
        A class to represent a node on a circle plot.

        Parameter(s):
        -------------
        node : Node
            A valid Node object, such as Node().
        index : Integer
            The index of the node on the plot.
        x : Float
            The x coordinate of the node.
        y : Float
            The y coordinate of the node.
        
        Object Propertie(s):
        --------------------
        node : Node
            The corresponding node object in the graph.
        label : String
            The label of the node on the plot.
        index : Integer
            The index of the node on the plot.
        x : Float
            The x coordinate of the node.
        y : Float
            The y coordinate of the node.
        color : String
            The color of the node on the plot.

        See also:
        ---------
            CircleEdge
            Circle
    """

    def __init__(self, node, index, x=0, y=0):
        self.node = node
        self.label = node.label
        self.index = index
        self.x = x
        self.y = y
        self.avg = 0
        self.color = index



class CircleEdge():
    """
        A class to represent an edge on a circle plot.

        Parameter(s):
        -------------
        edge : Edge
            A valid Edge object, such as TemporalEdge().
        label : String
            The label of the edge on the plot.
        p1 : Dict
            The p1 coordinate of the edge, as a dictionary with keys 'x' and 'y'.
        p2 : Dict
            The p2 coordinate of the edge, as a dictionary with keys 'x' and 'y'.
        
        Object Propertie(s):
        --------------------
        edge : Edge
            The corresponding edge object in the graph.
        index : Integer
            The index of the edge on the plot.
        p1 : Dict
            The p1 coordinate of the edge, as a dictionary with keys 'x' and 'y'.
        p2 : Dict
            The p2 coordinate of the edge, as a dictionary with keys 'x' and 'y'.

        See also:
        ---------
            CircleNode
            Circle
    """

    def __init__(self, edge, p1, p2):
        self.edge = edge
        self.label = edge.uid
        self.p1 = p1
        self.p2 = p2



class Circle(Plot):
    """
        A circle plot with the option of barycenter ordering.

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
            A switch to enable/disable barycenter ordering of the circle plot nodes.
        slider : Boolean
            Disabled.
        show : Boolean
            Show the plot (can be overridden).

        Object Propertie(s):
        --------------------
        name : String
            Inherited from Plot.
        graph : Graph
            Inherited from Plot.
        title : String
            Inherited from Plot.
        nodes : List
            Inherited from Plot.
        edges : List
            Inherited from Plot.
        labels : List
            Inherited from Plot.
        figure : Figure
            Inherited from Plot.
        axis : axis
            Inherited from Plot.
        is_ordered : Boolean
            Inherited from Plot.
        has_slider : Boolean
            Inherited from Plot.
        show : Boolean
            Inherited from Plot.


        See also:
        ---------
            CircleNode
            CircleEdge
            Plot
            Slice
    """
    class_name = 'circle'

    def __init__(self, graph, figure, axis, title=None, ordered=True, slider=False, show=True):
        super().__init__(graph, figure, axis, title, ordered, False, show)


    def create_nodes(self):
        n = self.graph.nodes.count()
        i = 0
        for node in self.graph.nodes.set:
            x = math.cos(2 * math.pi * i / n)
            y = math.sin(2 * math.pi * i / n)
            self.nodes.append(CircleNode(node, i, x, y))
            i += 1
        if self.is_ordered:
            self.order_nodes(self.graph.edges.count())


    def get_node(self, label):
        return next((node for node in self.nodes if node.label == label), None)


    def order_nodes(self, iterations):
        for x in range(iterations):
            self.nodes = sorted(self.nodes, key=lambda x:x.avg, reverse=False)
            n = self.graph.nodes.count()
            i = 0
            for node in self.nodes:
                if not node.index == i:
                    node.index = i
                    node.x = math.cos(2 * math.pi * i / n)
                    node.y = math.sin(2 * math.pi * i / n)
                sum_x = node.x
                sum_y = node.y
                for neighbour in node.node.neighbours().set:
                    sum_x = sum_x + self.get_node(neighbour.label).x
                    sum_y = sum_y + self.get_node(neighbour.label).y
                node.avg = vector_angle(sum_x, sum_y)
                i += 1


    def create_edges(self):
        for edge in self.graph.edges.set:
            p1 = {'x': self.get_node(edge.node1.label).x, 'y': self.get_node(edge.node1.label).y}
            p2 = {'x': self.get_node(edge.node2.label).x, 'y': self.get_node(edge.node2.label).y}
            self.edges.append(CircleEdge(edge, p1, p2))
            

    def draw_nodes(self):
        n = self.graph.nodes.count()
        pos = {}
        pos['x'] = [node.x for node in self.nodes]
        pos['y'] = [node.y for node in self.nodes]
        colors = [x for x in range(0, n)]
        cmap = self.set3colormap(n)
        ax_node = self.axis.scatter(
            pos['x'], pos['y'], s=500, c=colors, cmap=cmap, zorder=1
        )
        plt.draw()
        i = 0
        for node in self.nodes:
            node.color = ax_node.to_rgba(colors[i])
            self.axis.text(
                node.x, node.y,
                node.label, color='midnightblue',
                rotation=circle_label_angle(node.x, node.y),
                ha='center', va='center',
                fontsize='small'
            )
            i += 1


    def draw_edges(self):
        for edge in self.edges:
            edge_color = self.get_node(edge.edge.node1.label).color
            if edge.edge.directed:
                color=edge_color
            else:
                color='lightgrey'
            bezier_edge = bezier(edge.p1, edge.p2)
            self.axis.plot(
                bezier_edge['x'],
                bezier_edge['y'],
                linestyle='-',
                color=color,
                zorder=0
            )
            if edge.edge.directed:
                self.axis.plot(
                    bezier_edge['x'][6],
                    bezier_edge['y'][6],
                    'o',
                    color=edge_color,
                    zorder=1
                )
            if not self.graph.static:
                self.axis.text(
                    bezier_edge['x'][10], bezier_edge['y'][10],
                    edge.edge.start, 
                    color='midnightblue', backgroundcolor=edge_color,
                    fontsize='xx-small',
                    horizontalalignment='center',
                    rotation=circle_label_angle(bezier_edge['x'][11], bezier_edge['y'][11]),
                    zorder=1,
                )


    def cleanup(self):
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)
        self.remove_xticks(self.axis)
        self.remove_yticks(self.axis)
        self.set_aspect(self.axis)
        self.style_axis(self.axis)


    def remove_xticks(self, ax):
        ax.set_xticklabels([])
        ax.set_xticks([])


    def remove_yticks(self, ax):
        ax.set_yticklabels([])
        ax.set_yticks([])


    def set_aspect(self, ax):
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        ax.set_aspect((x1 - x0) / (y1 - y0))
        ax.margins(0.1, 0.1)


    def style_axis(self, ax):
        ax.set_facecolor('slategrey')
        for spine in ['top', 'bottom', 'right', 'left']:
            ax.spines[spine].set_color('lightgrey')
