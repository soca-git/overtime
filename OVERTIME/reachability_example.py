
import math
import numpy as np
import matplotlib.pyplot as plt

from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from algorithms.reachability import CalculateNodeReachability



tube = TemporalDiGraph('TubeNetwork', data=CSVInput('./tube.csv'))
tube.details()

R = []
for node in tube.nodes.set:
    R.append(CalculateNodeReachability(tube.get_graph_by_interval((850, 920)), node.label))


X = [x for x in range(0, tube.nodes.count())]
Y = np.random.rand(tube.nodes.count())
figure, axes = plt.subplots(1)

plt.subplots_adjust(left=0.05, bottom=0.2, right=0.95, top=0.95, wspace=0, hspace=0)
plt.scatter(
    X, Y,
    s = [(r+2)*30 for r in R],
    c=Y,
    alpha=0.5
)
axes.set_xticks(range(0, tube.nodes.count()))
axes.set_xticklabels(tube.nodes.labels(), fontsize=9)
axes.set_yticks([])
axes.set_yticklabels([])
plt.setp(axes.get_xticklabels(), rotation=90, fontsize=9)
axes.grid(color='lightgrey', linestyle='-', linewidth=0.1)
axes.set_facecolor('slategrey')


for n in range(0, len(X)):
    axes.text(
        X[n], Y[n],
        R[n], color='white',
        ha='center', va='center',
        fontsize='small'
    )

figure.show()

input("Press enter key to exit...")
