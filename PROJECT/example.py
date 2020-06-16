
from inputs.classes import CSVInput
from components.graphs import TemporalGraph

input_data = CSVInput('network', 'csv', './network.csv')

graph = TemporalGraph('TestNetwork', input_data)
