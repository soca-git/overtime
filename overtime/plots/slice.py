
#from random import shuffle
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib.widgets import Slider
from overtime.plots.plot import Plot



class SliceEdge():
    """
        A class to represent an edge on a slice plot.

        Parameter(s):
        -------------
        edge : Edge
            A valid temporal Edge object, such as TemporalEdge().
        index : Integer
            The index of the edge on the plot.
        x : Float
            The x coordinate of the edge.
        y : Float
            The y coordinate of the edge.
        
        Object Propertie(s):
        --------------------
        edge : Edge
            The corresponding edge object in the graph.
        index : Integer
            The index of the edge on the plot.
        x : Float
            The x coordinate of the edge.
        y : Float
            The y coordinate of the edge.
        color : String
            The color of the edge on the plot.

        See also:
        ---------
            Slice
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
        A slice plot for temporal networks.

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
        axis : Axis
            A pyplot axis object.
        title : String
            A custom title for the plot.
        ordered : Boolean
            Disabled.
        slider : Boolean
            Automatically enabled if number of ticks is deemed to be too many and will overlap otherwise.
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
        axis : Axis
            Inherited from Plot.
        is_ordered : Boolean
            Inherited from Plot.
        has_slider : Boolean
            Inherited from Plot.
        show : Boolean
            Inherited from Plot.


        See also:
        ---------
            SliceEdge
            Plot
            Circle
    """
    class_name = 'slice'

    def __init__(self, graph, figure, axis, title=None, ordered=False, slider=True, show=True):
        super().__init__(graph, figure, axis, title, False, slider, show)


    def create_edges(self):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, creates the SliceEdge objects.
        """
        step = 1 # step multiplier.
        # for each unique edge label (independent of time).
        for label in self.graph.edges.ulabels():
            self.labels.append(label) # append the edge label to the plot labels list.
        
        # for each timestep in the graph's timespan.
        for t in self.graph.edges.timespan():
            # for every edge in the graph.
            for edge in self.graph.edges.set:
                # if the edge is active at the 't'.
                if edge.isactive(t):
                    i = self.labels.index(edge.label) # get the index of the edge within self.labels.
                    # create a SliceEdge and add it to the edges list.
                    self.edges.append(SliceEdge(edge, i, x=(t*step), y=(i*step)))
        

    def draw_edges(self):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, draws the edges of the plot.
        """
        pos = {}
        pos['x'] = [edge.x for edge in self.edges] # x coordinates of every node.
        pos['y'] = [edge.y for edge in self.edges] # y coordinates of every node.
        colors = pos['y'] # colors index for every edge.
        cmap = self.set3colormap(len(self.labels)) # color map with enough colors for n edges.
        # draw the edges using pyplot scatter.
        self.axis.scatter(
            pos['x'], pos['y'], s=50, c=colors, cmap=cmap, zorder=1
        )
        plt.draw()


    def cleanup(self):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, updates figure & axis properties & styling.
        """
        # adjust whitespace around the plot.
        plt.subplots_adjust(left=0.25, bottom=0.15, right=0.95, top=0.95, wspace=0, hspace=0)
        self.figure.set_size_inches(32, 16) # set figure size.
        times = list(set([edge.x for edge in self.edges])) # get x-ticks.
        self.draw_xticks(self.axis, times) # draw x-ticks
        edge_ticks = [y for y in range(0, len(self.labels))] # get y-ticks.
        self.draw_yticks(self.axis, edge_ticks) # draw y-ticks.
        self.draw_grid(self.axis) # draw grid.
        self.style_axis(self.axis) # style axis.

        if self.has_slider:
            self.draw_sliders(times, edge_ticks, 79, 39) # draw sliders.
            pass
        if self.show:
            self.axis.set_xlabel('Time') # set x-axis label.
            self.axis.set_ylabel('Edge') # set y-axis label.


    def draw_xticks(self, ax, xticks):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, draws x-ticks and labels.
        """
        loc = plticker.MultipleLocator(base=1)
        ax.xaxis.set_major_locator(loc)
        ax.set_xticks(xticks)
        plt.setp(ax.get_xticklabels(), rotation=90, fontsize=9)


    def draw_yticks(self, ax, yticks):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, draws y-ticks and labels.
        """
        ax.set_yticks(yticks)
        ax.set_yticklabels(self.labels, fontsize=9)


    def draw_grid(self, ax):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, draws a grid.
        """
        ax.grid(color='lightgrey', linestyle='-', linewidth=0.1)


    def draw_sliders(self, xticks, yticks, xstep, ystep):
        """
            A method of Plot/Slice.

            Returns:
            --------
                None, draws sliders for the x-axis, y-axis, or both.
        """
        flag = False
        # if the plot has sliders enabled and the number of x-ticks is deemed large.
        if self.has_slider and len(xticks) > xstep:
            # set x-axis range.
            self.axis.set(xlim=(xticks[0]-1, xstep))
            axpos = plt.axes([0.325, 0.035, 0.55, 0.025]) # slider bbox position.
            # Create x-axis pyplot slider.
            xpos = Slider(axpos, 'Time', xticks[0]-1, xticks[-1]-xstep, color='aquamarine')
            # Update function for changes in x.
            def updatex(val):
                pos = xpos.val # position of slider (clickable).
                # maximum x-tick (influenced by figure window size).
                xtick_max = 4+pos+math.floor(self.figure.get_size_inches()[0]*4)
                # update x-axis range.
                self.axis.set(xlim=(pos, xtick_max))
                self.figure.canvas.draw_idle() # draw updates.
            
            # on clicking slider, update axis.
            xpos.on_changed(updatex)
            updatex((xticks[0]-1, xstep)) # initial update.
            # on figure window resize, update axis.
            self.figure.canvas.mpl_connect('resize_event', updatex)
            flag = True # flag a slider was created.
        
        # if the plot has sliders enabled and the number of y-ticks is deemed large.
        if self.has_slider and len(yticks) > ystep:
            # set y-axis range.
            self.axis.set(ylim=(yticks[0]-1, ystep))
            axpos = plt.axes([0.025, 0.25, 0.0125, 0.6]) # slider bbox position.
            # Create y-axis pyplot slider.
            ypos = Slider(axpos, 'Edge', yticks[0]-1, yticks[-1]-ystep, orientation='vertical', color='mediumspringgreen')
            # Update function for changes in y.
            def updatey(val):
                pos = ypos.val # position of slider (clickable).
                # maximum y-tick (influenced by figure window size).
                ytick_max = 4+pos+math.floor(self.figure.get_size_inches()[1]*4)
                # update y-axis range.
                self.axis.set(ylim=(pos, ytick_max))
                self.figure.canvas.draw_idle() # draw updates.
            
            # on clicking slider, update axis.
            ypos.on_changed(updatey)
            updatey((yticks[0]-1, ystep)) # initial update.
            self.figure.canvas.mpl_connect('resize_event', updatey)
            # on figure window resize, update axis.
            flag = True # flag a slider was created.

        # if a slider was created, we need to run plt.show() now to allow user interaction.
        if flag:
            print('plt.show() activated. Please close the figure(s) in order to continue.')
            self.show = False # plotter no longer needs to call figure.show()
            plt.show()
