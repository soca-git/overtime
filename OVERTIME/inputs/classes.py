
import csv



class Input:
    """
        A class which handles temporal network/data inputs.
    """

    def __init__(self, path):
        self.path = path
        self.data = {}
        self.data['nodes'] = {}
        self.data['edges'] = {}



class CSVInput(Input):
    """
        A class which handles CSV-based temporal network/data inputs.
    """

    def __init__(self, path):
        super().__init__(path)
        self.read()


    def read(self):
        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = self.data
            ne = 0
            for row in reader:
                data['edges'][ne] = {}
                data['edges'][ne]['node1'] = row['node1']
                data['edges'][ne]['node2'] = row['node2']
                data['edges'][ne]['tstart'] = row['tstart']
                if 'end' in row:
                    data['edges'][ne]['tend'] = row['tend']
                else:
                    data['edges'][ne]['tend'] = None
                ne += 1
