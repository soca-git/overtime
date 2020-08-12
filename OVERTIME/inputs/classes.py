
import csv
import datetime
import re
from inputs.rest import TflRest



class Input:
    """
        A class which handles temporal network/data inputs.
    """

    def __init__(self):
        self.data = {}
        self.data['nodes'] = {}
        self.data['edges'] = {}



class CSVInput(Input):
    """
        A class which handles CSV-based temporal network/data inputs.
    """

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.read()


    def read(self):
        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = self.data
            ne = 0
            for row in reader:
                if any(x.strip() for x in row):
                    data['edges'][ne] = {}
                    data['edges'][ne]['node1'] = row['node1']
                    data['edges'][ne]['node2'] = row['node2']
                    data['edges'][ne]['tstart'] = row['tstart']
                    if 'tend' in row:
                        data['edges'][ne]['tend'] = row['tend']
                    else:
                        data['edges'][ne]['tend'] = None
                    ne += 1



class TubeInput(Input):
    """
        A class used to create input data from the tube network.
    """

    def __init__(self, lines, times, path='tube.csv'):
        super().__init__()
        self.api = TflRest()
        self.lines = lines
        self.times = times
        self.path = path
        for line in lines:
            for time in times:
                self.generate_journeys(line, time)
            

    def generate_journeys(self, line_name, time):
        endpoints = self.get_endpoints(line_name)
        for direction, stations in endpoints.items():
            line = self.get_journey(stations['origin'], stations['destination'], time)
            print(line)
            print('{} ---> {}, {} ({} mins)'.format(stations['origin'], stations['destination'], direction, line['duration']))
            current_time = time
            for n in range(0, len(line['stops'])):
                try:
                    journey = self.get_journey(line['stops'][n], line['stops'][n+1], current_time)
                    current_time = self.update_time(journey['arrivalDateTime'])
                    self.data['edges']["-".join([line_name, direction, str(current_time)])] = {
                        'node1': journey['stations'][0],
                        'node2': journey['stations'][-1],
                        'tstart': self.convert_time(journey['startDateTime']),
                        'tend': self.convert_time(journey['arrivalDateTime']),
                        'line': journey['name']
                    }
                    self.write_csv()
                except IndexError:
                    break


    def get_endpoints(self, line):
        endpoints = {}
        line = self.api.get_line(line)
        for route in line['routeSections']:
            endpoints[route['direction']] = {
                'origin': route['originator'],
                'destination': route['destination']
            }
        return endpoints


    def get_journey(self, origin, destination, time):
        response = self.api.get_journey(origin, destination, time)
        jdata = {}
        for journey in response['journeys']:
            jdata = {
                'startDateTime': journey['startDateTime'],
                'arrivalDateTime': journey['arrivalDateTime']
            }
            for leg in journey['legs']:
                if 'Walk' in leg['instruction']['summary']:
                    continue
                try:
                    jdata['name'] = leg['instruction']['summary']
                    jdata['departurePoint'] = leg['departurePoint']['naptanId']
                    jdata['arrivalPoint'] = leg['arrivalPoint']['naptanId']
                    jdata['duration'] = leg['duration']
                    jdata['stops'] = [origin]
                    jdata['stations'] = [leg['departurePoint']['commonName'].replace(' Underground Station', '')]
                    for station in leg['path']['stopPoints']:
                        jdata['stops'].append(station['id'])
                        jdata['stations'].append(station['name'].replace(' Underground Station', ''))
                except KeyError:
                    continue
        return jdata


    def update_time(self, time):
        time = [int(i) for i in re.split('T|-|:', time)]
        time = datetime.datetime(time[0], time[1], time[2], time[3], time[4])
        delta = datetime.timedelta(minutes=1)
        time = time - delta
        return "".join(str(time).split(' ')[-1].split(':')[0:2])


    def convert_time(self, time):
        time = time.split('T')[-1].split(':')[0:2]
        hours = int(time[0])
        minutes = int(time[1])
        return minutes + hours * 60


    def write_csv(self):
        cols = ['node1', 'node2', 'tstart', 'tend', 'line']
        try:
            with open(self.path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=cols)
                writer.writeheader()
                for key, data in self.data['edges'].items():
                    writer.writerow(data)

        except IOError:
            print("I/O Error; error writing to csv.")


    def print(self):
        for id, edge in self.data['edges'].items():
            print(id)
            print('{}({}) --> {}({})'.format(edge['node1'], edge['tstart'], edge['node2'], edge['tend']))
