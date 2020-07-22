
import math
import matplotlib.pyplot as plt


class Plotter:
    """
        A class for creating various plots.
    """

    def __init__(self):
        self.plot = None


    def single(self, plot, graph):
        self.plot = plot
        figure, axes = plt.subplots(1)
        self.plot(graph, axes, graph.label)
        plt.tight_layout(pad=0.1)
        figure.set_size_inches(14, 10)
        figure.show()


    def multi(self, plot, graphs):
        self.plot = plot
        ncols = math.ceil(math.sqrt(len(graphs)))
        nrows = math.ceil(len(graphs)/ncols)
        figure, axes = plt.subplots(nrows, ncols)
        i = 0
        flag = False
        for row in axes:
            if nrows == 1:
                self.plot(graphs[i], row, graphs[i].label)
                i += 1
                if i == len(graphs):
                    flag = True
                    break
            else:
                for col in row:
                    self.plot(graphs[i], col, graphs[i].label)
                    i += 1
                    if i == len(graphs):
                        flag = True
                        break
            if flag:
                break
        
        extra_axes = nrows * ncols - len(graphs)
        for x in range(ncols-extra_axes, ncols):
            figure.delaxes(axes[nrows-1][x])
        figure.set_size_inches(14, 10)
        figure.show()
