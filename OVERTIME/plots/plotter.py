
import math
import matplotlib.pyplot as plt
import imageio



class Plotter:
    """
        A class for creating various plots.
    """

    def __init__(self):
        self.plot = None


    def single(self, plot, graph, save=False, ordered=True, slider=True):
        self.plot = plot
        figure, axes = plt.subplots(1)
        figure.set_size_inches(14, 10)
        plot_object = self.plot(graph, figure, axes, graph.label, ordered=ordered, slider=slider)    
        if save:
            self.save(figure, plot.name, graph.label)
        elif not plot_object.shown:
            figure.show()


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
        figure.set_size_inches(14, 10)
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
        plt.tight_layout(pad=0.1)
        if save:
            self.save(figure, plot.name, file_name)
        else:
            figure.show()


    def save(self, figure, plot_name, label):
        def update_label(label):
            return label.replace(' ', '_').replace(':','').replace(',','')

        label = update_label(label)
        plot_name = update_label(plot_name)
        figure.savefig(label + '-' + plot_name + '.png', format='png')
