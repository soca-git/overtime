
import numpy as np
import math
import matplotlib.pyplot as plot

class Circle:
    """
        A class which represents a circle plot of a graph.
    """

    def __init__(self, graph):
        self.graph = graph
        self.nodes = {}
        self.edges = {}
        self.fig, self.ax = plot.subplots(1)
        self.create()


    def create(self):
        graph = self.graph
        nodes = self.nodes
        n = graph.nodes.count()
        i = 0
        for node in graph.nodes.set:
            nodes[node.label] = {}
            nodes[node.label]['x'] = math.cos(2 * math.pi * i / n)
            nodes[node.label]['y'] = math.sin(2 * math.pi * i / n)
            self.ax.scatter(
                nodes[node.label]['x'], nodes[node.label]['y'], s=500, zorder=1
            )
            self.ax.text(
                nodes[node.label]['x']-0.025, nodes[node.label]['y']-0.025,
                node.label, color='white'
            )
            i += 1

        self.cleanup()


    def cleanup(self):
        ax = self.ax
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_frame_on(False)
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        ax.set_aspect((x1 - x0) / (y1 - y0))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)


    def display(self):
        self.fig.show()
