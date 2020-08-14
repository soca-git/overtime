
#from random import shuffle
import math
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

    def __init__(self, graph, figure, axes, title=None, time=None, ordered=False, slider=True):
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
        plt.subplots_adjust(left=0.25, bottom=0.15, right=0.95, top=0.95, wspace=0, hspace=0)
        self.figure.set_size_inches(32, 16)
        times = list(set([edge.x for edge in self.edges]))
        self.draw_xticks(self.axes, times)
        edge_ticks = [y for y in range(0, len(self.labels))]
        self.draw_yticks(self.axes, edge_ticks)
        self.draw_grid(self.axes)
        self.style_axis(self.axes)

        if self.has_slider:
            self.draw_sliders(times, edge_ticks, 79, 39)
        if not self.shown:
            self.axes.set_xlabel('Time')
            self.axes.set_ylabel('Edge')


    def draw_xticks(self, ax, xticks):
        loc = plticker.MultipleLocator(base=1)
        ax.xaxis.set_major_locator(loc)
        ax.set_xticks(xticks)
        plt.setp(ax.get_xticklabels(), rotation=90, fontsize=9)


    def draw_yticks(self, ax, yticks):
        ax.set_yticks(yticks)
        ax.set_yticklabels(self.labels, fontsize=9)


    def draw_grid(self, ax):
        ax.grid(color='lightgrey', linestyle='-', linewidth=0.1)


    def style_axis(self, ax):
        ax.set_facecolor('slategrey')
        for spine in ['top', 'bottom', 'right', 'left']:
            ax.spines[spine].set_color('lightgrey')
    

    def draw_sliders(self, xticks, yticks, xstep, ystep):
        flag = False
        if self.has_slider and len(xticks) > xstep:
            self.axes.set(xlim=(xticks[0]-1, xstep))
            axpos = plt.axes([0.325, 0.035, 0.55, 0.025])
            xpos = Slider(axpos, 'Time', xticks[0]-1, xticks[-1]-xstep, color='aquamarine')
            def updatex(val):
                pos = xpos.val
                xtick_max = 4+pos+math.floor(self.figure.get_size_inches()[0]*4)
                self.axes.set(xlim=(pos, xtick_max))
                self.figure.canvas.draw_idle()
            xpos.on_changed(updatex)
            updatex((xticks[0]-1, xstep))
            self.figure.canvas.mpl_connect('resize_event', updatex)
            flag = True
        
        if self.has_slider and len(yticks) > ystep:
            self.axes.set(ylim=(yticks[0]-1, ystep))
            axpos = plt.axes([0.025, 0.25, 0.0125, 0.6])
            ypos = Slider(axpos, 'Edge', yticks[0]-1, yticks[-1]-ystep, orientation='vertical', color='mediumspringgreen')
            def updatey(val):
                pos = ypos.val
                ytick_max = 4+pos+math.floor(self.figure.get_size_inches()[1]*4)
                self.axes.set(ylim=(pos, ytick_max))
                self.figure.canvas.draw_idle()
            ypos.on_changed(updatey)
            updatey((yticks[0]-1, ystep))
            self.figure.canvas.mpl_connect('resize_event', updatey)
            flag = True

        if flag:
            print('plt.show() activated. Please close the figure(s) in order to continue.')
            self.shown = True
            plt.show()
