
import csv



class Input:
    """
        A class which handles temporal network/data inputs.
    """

    def __init__(self, name, atype):
        self.name = name
        self.type = atype



class CSVInput(Input):
    """
        A class which handles CSV-based temporal network/data inputs.
    """

    def __init__(self, name, atype, path):
        super().__init__(name, atype)
        self.path = path
        self.data = {}


    def read(self):
        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            n = 0
            data = {}
            for row in reader:
                data[n] = {}
                data[n]['source'] = row['source']
                data[n]['sink'] = row['sink']
                data[n]['time'] = row['time']
                n += 1
        self.data = data

    
    def print(self):
        with open(self.path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
