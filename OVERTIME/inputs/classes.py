
import csv
from time import sleep
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

    def __init__(self, lines, times):
        super().__init__()
        self.api = TflRest()
        self.lines = lines
        self.times = times
        for line in lines:
            for time in times:
                self.generate_journeys(line, time)
            

    def get_endpoints(self, line):
        endpoints = {}
        line = self.api.get_line(line)
        for route in line['routeSections']:
            endpoints[route['direction']] = {
                'origin': route['originator'],
                'destination': route['destination']
            }
        return endpoints


    def generate_journeys(self, line_name, time):
        endpoints = self.get_endpoints(line_name)
        for direction, stations in endpoints.items():
            line = self.get_journey(stations['origin'], stations['destination'], time)
            for x, line_journey in line.items():
                print(line_journey)
                print('{} ---> {}, {} ({} mins)'.format(stations['origin'], stations['destination'], direction, line_journey['duration']))
                current_time = time
                for n in range(0, len(line_journey['stops'])):
                    try:
                        for i, journey in self.get_journey(line_journey['stops'][n], line_journey['stops'][n+1], current_time).items():
                            sleep(1)
                            current_time = self.get_time(journey['startDateTime'])
                            self.data['edges']["-".join([line_name, direction, str(current_time)])] = {
                                'node1': journey['stations'][0],
                                'node2': journey['stations'][-1],
                                'tstart': self.convert_time(journey['startDateTime']),
                                'tend': self.convert_time(journey['arrivalDateTime'])
                            }
                    except IndexError:
                        break


    def get_time(self, time):
        return "".join(time.split('T')[-1].split(':')[0:2])


    def convert_time(self, time):
        time = time.split('T')[-1].split(':')[0:2]
        hours = int(time[0])
        minutes = int(time[1])
        return minutes + hours * 60


    def get_journey(self, origin, destination, time):
        journey_data = {}
        response = self.api.get_journey(origin, destination, time)
        n = 0
        for journey in response['journeys']:
            journey_data[n] = {
                'startDateTime': journey['startDateTime'],
                'arrivalDateTime': journey['arrivalDateTime']
            }
            for leg in journey['legs']:
                #print(leg)
                journey_data[n]['name'] = leg['instruction']['summary']
                journey_data[n]['departurePoint'] = leg['departurePoint']['naptanId']
                journey_data[n]['arrivalPoint'] = leg['arrivalPoint']['naptanId']
                journey_data[n]['duration'] = leg['duration']
                journey_data[n]['stops'] = [origin]
                journey_data[n]['stations'] = [leg['departurePoint']['commonName'].replace(' Underground Station', '')]
                for station in leg['path']['stopPoints']:
                    journey_data[n]['stops'].append(station['id'])
                    journey_data[n]['stations'].append(station['name'].replace(' Underground Station', ''))
                #n += 1
        return journey_data


    def print(self):
        for id, edge in self.data['edges'].items():
            print(id)
            print('{}({}) --> {}({})'.format(edge['node1'], edge['tstart'], edge['node2'], edge['tend']))
