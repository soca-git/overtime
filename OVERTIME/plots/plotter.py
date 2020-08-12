
import math
import matplotlib.pyplot as plt
import imageio



class Plotter:
    """
        A class for creating various plots.
    """

    def __init__(self):
        self.plot = None


    def single(self, plot, graph, save=False, ordered=True, slider=False):
        self.plot = plot
        figure, axes = plt.subplots(1)
        plt.subplots_adjust(left=0.18, bottom=0.1, right=0.95, top=0.95, wspace=0, hspace=0)
        self.plot(graph, figure, axes, graph.label, ordered=ordered, slider=slider)    
        if save:
            self.save(figure, plot.name, graph.label)


    def singles(self, plot, graphs, save=False):
        for graph in graphs:
            self.single(plot, graph, save)


    def gif(self, plot, graphs, save=False, ordered=True, file_name='graph'):
        for graph in graphs:
            self.single(plot, graph, save=True, ordered=ordered)
        labels = [file_name + '/' + graph.label + '.png' for graph in graphs]
        images = [imageio.imread(f) for f in labels]
        imageio.mimsave(file_name + '/' + file_name + '.gif', images, duration=2)


    def multi(self, plot, graphs, save=False, ordered=True, file_name='multi'):
        self.plot = plot
        ncols = math.ceil(math.sqrt(len(graphs)))
        nrows = math.ceil(len(graphs)/ncols)
        figure, axes = plt.subplots(nrows, ncols)
        i = 0
        flag = False
        for row in axes:
            if nrows == 1:
                self.plot(graphs[i], figure, row, graphs[i].label, ordered=ordered)
                i += 1
                if i == len(graphs):
                    flag = True
                    break
            else:
                for col in row:
                    self.plot(graphs[i], figure, col, graphs[i].label, ordered=ordered)
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
        def update_label(label):
            return label.replace(' ', '_').replace(':','').replace(',','')

        label = update_label(label)
        plot_name = update_label(plot_name)
        figure.savefig(label + '-' + plot_name + '.png', format='png')
