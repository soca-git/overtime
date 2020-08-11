
import requests as reqs



class Rest:
    """
        A class for handling rest api interactions.
    """

    def __init__(self, base_url):
        self.base = str(base_url)


    def get(self, url, query=''):
        return reqs.get(self.base + url + query).json()



class TflRest(Rest):
    """
        A class for handling TFL rest api interactions.
    """

    def __init__(self):
        super().__init__('https://api.tfl.gov.uk/')


    def get_line(self, name):
        return reqs.get(self.base + 'Line/' + name + '/Route/').json()


    def get_station_by_name(self, name):
        return reqs.get(self.base + 'StopPoint/Search/' + name).json()['matches'][0]


    def get_line_stations(self, line):
        return reqs.get(self.base + 'Line/' + line + '/StopPoints').json()


    def get_line_sequence(self, line, direction):
        return reqs.get(self.base + 'Line/' + line + '/Route/Sequence/' + direction).json()


    def get_journey(self, from_id, to_id, time, timel='departing'):
        return reqs.get(
            self.base + '/Journey/JourneyResults/' + from_id + '/to/' + to_id
            + '?mode=tube'
            + '&useMultiModalCall=false'
            + '&routeBetweenEntrances=false'
            + '&journeypreference=leastwalking'
            + '&time=' + time
            + '&timel=' + timel
        ).json()
