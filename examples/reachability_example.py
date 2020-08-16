
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from algorithms.reachability import calculate_reachability


tube = TemporalDiGraph('TubeNetwork', data=CSVInput('./victoria_bakerloo.csv'))
tube.details()

station_df = pd.read_csv("stations_victoria_bakerloo.csv")
tube.nodes.add_data(station_df)


R = []
for node in tube.nodes.set:
    R.append(calculate_reachability(tube, node.label))


X = [node.data['lon'] for node in tube.nodes.set]
Y = [node.data['lat'] for node in tube.nodes.set]
figure, axes = plt.subplots(1)

plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)
axes.set_aspect('equal')
plt.scatter(
    X, Y,
    s = [(r+2)*30 for r in R],
    c=Y,
    alpha=0.5
)
#axes.set_xticks(range(0, tube.nodes.count()))
#axes.set_xticklabels(tube.nodes.labels(), fontsize=9)
axes.set_xticks([])
axes.set_yticks([])
axes.set_xticklabels([])
axes.set_yticklabels([])
plt.setp(axes.get_xticklabels(), rotation=90, fontsize=9)
axes.grid(color='lightgrey', linestyle='-', linewidth=0.1)
axes.set_facecolor('slategrey')

n = 0
for node in tube.nodes.set:
    axes.text(
        X[n], Y[n],
        node.label + '\n' + str(R[n]), color='white',
        ha='center', va='center',
        fontsize='small'
    )
    n += 1

figure.set_size_inches(28, 20)
figure.savefig('reachability_example.png', format='png')
figure.show()

input("Press enter key to exit...")
