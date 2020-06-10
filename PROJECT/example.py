
from inputs.classes import CSVInput

network_csv = CSVInput('network', 'csv', './network.csv')
network_csv.print()
network_csv.read()

for i, tedge in network_csv.data.items():
    print(tedge)
