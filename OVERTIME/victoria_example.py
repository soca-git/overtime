
import pandas as pd

from inputs.classes import CSVInput
from components.digraphs import TemporalDiGraph
from plots.plotter import Plotter
from plots.circle import Circle
from plots.slice import Slice
from algorithms.foremost import CalculateForemostTree


tube = TemporalDiGraph('TubeNetwork', data=CSVInput('./victoria.csv'))
tube.details()


station_df = pd.read_csv("stations_victoria.csv")

tube.nodes.add_data(station_df)

