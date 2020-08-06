
import math
import matplotlib.pyplot as plt
import imageio



class Plotter:
    """
        A class for creating various plots.
    """

    def __init__(self):
        self.plot = None


    def single(self, plot, graph, save=False):
        self.plot = plot
        figure, axes = plt.subplots(1)
        self.plot(graph, axes, graph.label)
        figure.set_size_inches(7, 5)
        figure.show()
        if save:
            self.save(figure, plot.name, graph.label)


    def singles(self, plot, graphs, save=False):
        for graph in graphs:
            self.single(plot, graph, save)


    def gif(self, plot, graphs, save=False, file_name='graph'):
        for graph in graphs:
            self.single(plot, graph, True)
        labels = [file_name + '/' + graph.label + '.png' for graph in graphs]
        images = [imageio.imread(f) for f in labels]
        imageio.mimsave(file_name + '/' + file_name + '.gif', images, duration=2)


    def multi(self, plot, graphs, save=False, file_name='multi'):
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
        plt.tight_layout(pad=0.1)
        figure.show()
        if save:
            self.save(figure, plot.name, file_name)


    def save(self, figure, plot_name, label):
        figure.savefig(label + '_' + plot_name + '.png', format='png')
