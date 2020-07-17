
import math
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.lines as lines

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
        edges = self.edges
        n = graph.nodes.count()

        i = 0
        for node in graph.nodes.set:
            nodes[node.label] = {}
            nodes[node.label]['x'] = math.cos(2 * math.pi * i / n)
            nodes[node.label]['y'] = math.sin(2 * math.pi * i / n)
            i += 1
            
        for edge in graph.edges.stream:
            edges[edge.uid] = {}
            edges[edge.uid]['p1'] = {}
            edges[edge.uid]['p1']['x'] = nodes[edge.source.label]['x']
            edges[edge.uid]['p1']['y'] = nodes[edge.source.label]['y']
            edges[edge.uid]['p2'] = {}
            edges[edge.uid]['p2']['x'] = nodes[edge.sink.label]['x']
            edges[edge.uid]['p2']['y'] = nodes[edge.sink.label]['y']

        
        self.draw_figure(graph)
        self.draw_nodes(graph, nodes, edges, n)
        self.draw_edges(graph, nodes, edges)
        self.cleanup()


    def draw_figure(self, graph):
        title = 'time(s) ' + str(graph.edges.active_times())
        self.ax.set_title(
            label=title,
            loc='center'
        )


    def draw_nodes(self, graph, nodes, edges, n):
        pos = {}
        pos['x'] = [nodes[key]['x'] for key in nodes.keys()]
        pos['y'] = [nodes[key]['y'] for key in nodes.keys()]

        colors = self.colors(n)
        ax_node = self.ax.scatter(
            pos['x'], pos['y'], s=500, c=colors, cmap='viridis', zorder=1
        )
        plot.draw()

        i = 0
        for node in self.graph.nodes.set:
            nodes[node.label]['color'] = ax_node.to_rgba(colors[i])
            self.ax.text(
                nodes[node.label]['x']-0.025, nodes[node.label]['y']-0.025,
                node.label, color='white'
            )
            i += 1


    def colors(self, n):
        c = [(1/n * x) for x in range(0, n)]
        c_mix = [0.0]
        for i in range(1,n):
            if i % 2 == 0:
                c_mix.append(c[i-1])
            else:
                c_mix.append(c[n-i])
        return c_mix


    def draw_edges(self, graph, nodes, edges):
        for edge in graph.edges.stream:
            bezier = self.bezier(
                edges[edge.uid]['p1'],
                edges[edge.uid]['p2']
            )
            self.ax.plot(
                bezier['x'],
                bezier['y'],
                linestyle='-',
                color=nodes[edge.source.label]['color'],
                zorder=0
            )
            self.ax.plot(
                bezier['x'][6],
                bezier['y'][6],
                'o',
                color=nodes[edge.source.label]['color'],
                zorder=1
            )
            # self.ax.text(
            #     bezier['x'][10], bezier['y'][10],
            #     edge.time, 
            #     color='black', backgroundcolor='white',
            #     fontsize='x-small',
            #     zorder=1
            # )


    def bezier(self, p1, p2, p0=(0,0), nt=20):
        bezier = {}
        bezier['x'] = []
        bezier['y'] = []
        for i in range(0, nt+1):
            t = (1/nt) * i
            bezier['x'].append(
                (p1['x']-2*p0[0]+p2['x'])*math.pow(t,2) + 2*t*(p0[0]-p1['x']) + p1['x']
            )
            bezier['y'].append(
                (p1['y']-2*p0[0]+p2['y'])*math.pow(t,2) + 2*t*(p0[0]-p1['y']) + p1['y']
            )
        return bezier


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
        #self.fig.show()
        pass
