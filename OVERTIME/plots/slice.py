
#from random import shuffle
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib.widgets import Slider
from plots.plot import Plot



class SliceEdge():
    """
        A class to represent a node on a slice plot.
    """

    def __init__(self, edge, index, x=0, y=0):
        self.edge = edge
        self.label = edge.label
        self.index = index
        self.x = x
        self.y = y
        self.color = 'red'



class Slice(Plot):
    """
        A class which represents a slice plot of a graph.
    """
    name = 'slice'

    def __init__(self, graph, figure, axes, title=None, time=None, ordered=False, slider=False):
        super().__init__(graph, figure, axes, title, time, False, slider)


    def create_edges(self):
        step = 1
        for label in self.graph.edges.ulabels():
            self.labels.append(label)
        
        for t in self.graph.edges.timespan():
            for edge in self.graph.edges.set:
                if edge.isactive(t):
                    i = self.labels.index(edge.label)
                    self.edges.append(SliceEdge(edge, i, x=(t*step), y=(i*step)))
        

    def draw_edges(self):
        pos = {}
        pos['x'] = [edge.x for edge in self.edges]
        pos['y'] = [edge.y for edge in self.edges]
        colors = pos['y']
        cmap = self.set3colormap(self.graph.edges.count())
        self.axes.scatter(
            pos['x'], pos['y'], s=50, c=colors, cmap=cmap, zorder=1
        )
        plt.draw()


    def cleanup(self):
        ax = self.axes
        times = list(set([edge.x for edge in self.edges]))
        loc = plticker.MultipleLocator(base=1)
        ax.xaxis.set_major_locator(loc)
        ax.set_xticks(times)
        label_ticks = [y for y in range(0, len(self.labels))]
        ax.set_yticks(label_ticks)
        ax.set_yticklabels(self.labels)
        #ax.set_xlabel('Time')
        ax.set_ylabel('Edge')
        ax.grid(color='lightgrey', linestyle='-', linewidth=0.1)
        ax.set_facecolor('slategrey')
        plt.setp(ax.get_xticklabels(), rotation=90)
        self.figure.set_size_inches(32, 16)
        for spine in ['top', 'bottom', 'right', 'left']:
            ax.spines[spine].set_color('lightgrey')
        if self.has_slider:
            self.slider(times[0]-1, times[-1]+1, 100)


    def slider(self, min, max, step):
        self.axes.set(xlim=(min-1, step))
        axpos = plt.axes([0.2, 0.025, 0.65, 0.03])
        tpos = Slider(axpos, 'Time', min, max)
        def update(val):
            pos = tpos.val
            self.axes.set(xlim=(pos, pos+step))
            self.figure.canvas.draw_idle()
        tpos.on_changed(update)
        plt.show()
