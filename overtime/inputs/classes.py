
from os import path as ospath
import csv
import datetime
import re
from overtime.inputs.rest import TflRest



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
        self.path = "_".join(lines) + '.csv'

        if not ospath.exists(self.path):
            for line in lines:
                for direction in ['inbound', 'outbound']:
                    for time in times:
                        self.generate(line, direction, time)
        else:
            print("{} already exists.".format(self.path))


    def generate(self, line_name, direction, time):
        line_stations = self.get_line_routes(line_name, direction)
        for name, stations in line_stations.items():
            print('\n<<< {} ({}), {} @ {} >>>\n'.format(name, line_name, direction, time))
            current_time = time
            for n in range(0, len(stations)):
                try:
                    journey = self.get_journey(stations[n], stations[n+1], current_time)
                    if not journey or 'Walk' in journey['name']:
                        print('No available line from {} to {}.'.format(journey['departurePoint'], journey['arrivalPoint']))
                        continue
                    print('{} ---> {}, {} ({} mins)'.format(journey['departurePoint'], journey['arrivalPoint'], journey['name'], journey['duration']))
                    current_time = self.update_time(journey['arrivalDateTime'])
                    self.add_journey(
                        journey['departurePoint'],
                        journey['arrivalPoint'],
                        self.convert_time(journey['startDateTime']),
                        self.convert_time(journey['arrivalDateTime']),
                        journey['name'],
                        direction,
                        current_time
                    )
                    self.add_station(journey['departurePoint'], stations[n], journey['departurePointLocation'][0], journey['departurePointLocation'][1])
                    self.add_station(journey['arrivalPoint'], stations[n+1], journey['arrivalPointLocation'][0], journey['arrivalPointLocation'][1])
                except IndexError:
                    break
            self.write_stations_csv()
            self.write_journeys_csv()


    def get_line_routes(self, line, direction):
        response = self.api.get_line_sequence(line, direction)
        rdata = {}
        for route in response['orderedLineRoutes']:
            rdata[route['name']] = route['naptanIds']

        return rdata


    def get_journey(self, origin, destination, time):
        response = self.api.get_journey(origin, destination, time)
        jdata = {}
        n = 0
        for journey in response['journeys']:
            for leg in journey['legs']:
                departure_name = leg['departurePoint']['commonName'].replace(' Underground Station', '')
                arrival_name = leg['arrivalPoint']['commonName'].replace(' Underground Station', '')
                jdata[n] = {
                    'startDateTime': journey['startDateTime'],
                    'arrivalDateTime': journey['arrivalDateTime'],
                    'name': leg['instruction']['summary'],
                    'departurePoint': departure_name,
                    'arrivalPoint': arrival_name,
                    'duration': leg['duration'],
                    'departurePointLocation': (leg['departurePoint']['lat'], leg['departurePoint']['lon']),
                    'arrivalPointLocation': (leg['arrivalPoint']['lat'], leg['arrivalPoint']['lon'])
                }
            n += 1

        return jdata[0]


    def add_station(self, label, naptan_id, lat, lon):
        self.data['nodes'][label] = {
                'label': label,
                'id': naptan_id,
                'lat': lat,
                'lon': lon
        }


    def add_journey(self, node1, node2, tstart, tend, line, direction, time):
        self.data['edges']["-".join([line, direction, str(time)])] = {
            'node1': node1,
            'node2': node2,
            'tstart': tstart,
            'tend': tend,
            'line': line,
        }


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


    def write_journeys_csv(self):
        cols = ['node1', 'node2', 'tstart', 'tend', 'line']
        try:
            with open(self.path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=cols)
                writer.writeheader()
                for key, data in self.data['edges'].items():
                    writer.writerow(data)

        except IOError:
            print("I/O Error; error writing to csv.")


    def write_stations_csv(self):
        cols = ['label', 'id', 'lat', 'lon']
        try:
            with open('stations_' + self.path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=cols)
                writer.writeheader()
                for key, data in self.data['nodes'].items():
                    writer.writerow(data)

        except IOError:
            print("I/O Error; error writing to csv.")


    def print(self):
        for id, edge in self.data['edges'].items():
            print(id)
            print('{}({}) --> {}({})'.format(edge['node1'], edge['tstart'], edge['node2'], edge['tend']))
