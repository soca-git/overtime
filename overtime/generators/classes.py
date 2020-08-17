


class Generator:
    """
        Base class for generators.

        Object Propertie(s):
        ------------------
        data (Dict): A dictionary to hold all the node & edge information.

        See also:
        ---------
        RandomGNP
    """

    def __init__(self):
        self.data = {}
        self.data['nodes'] = {}
        self.data['edges'] = {}
