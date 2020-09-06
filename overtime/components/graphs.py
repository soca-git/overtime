
from overtime.components.nodes import Nodes
from overtime.components.edges import Edges, TemporalEdges



class Graph:
    """
        A class which represents a static, undirected graph consisting of nodes and edges.

        Parameter(s):
        -------------
        label : String
            A label for the graph.
        data : Input
            A valid Input class/subclass.

        Object Propertie(s):
        --------------------
        label : String
            The label of the graph.
        directed : Boolean
            Indicates whether the graph directed, or undirected.
        static : Boolean
            Indicates whether the graph is static, or not (temporal).
        nodes : Nodes
            A nodes collection representing all nodes in the graph.
        edges : Edges
            An edges collection representing all edges in the graph.

        See also:
        ---------
            TemporalGraph
            Digraph
            TemporalDiGraph
    """

    def __init__(self, label, data=None):
        self.label = label
        self.directed = False
        self.static = True
        self.nodes = Nodes(self)
        self.edges = Edges(self)

        # if input data is supplied.
        if data is not None:
            # build the graph using this data.
            self.build(data)


    def build(self, data):
        """
            A method of Graph.

            Parameter(s):
            -------------
            data : Input
                A valid Input class/subclass.

            Returns:
            --------
                None, adds edges & nodes to the graph.
        """
        # for each edge in data['edges'].
        for index, edge in data.data['edges'].items():
            # add the edge using the add_edge method.
            self.add_edge(edge['node1'], edge['node2'])
        # for each node in data['nodes'].
        for index, node in data.data['nodes'].items():
            self.add_node(node)


    def add_node(self, label):
        """
            A method of Graph.

            Parameter(s):
            -------------
            label : String
                The label of the node to be added.
            Returns:
            --------
            node : Node
                The corresponding node object.
        """
        return self.nodes.add(label)


    def add_edge(self, node1, node2):
        """
            A method of Graph.

            Parameter(s):
            -------------
            node1 : String
                The label of the node1 connection.
            node2 : String
                The label of the node2 connection.

            Returns:
            --------
            edge : Edge
                The corresponding edge object.
        """
        return self.edges.add(node1, node2, self.nodes)


    def remove_node(self, label):
        """
            A method of Graph.

            Parameter(s):
            -------------
            label : String
                The label of the node to be removed.
            
            Returns:
            --------
            None, removes the corresponding node and any connected edges (if the node exists in the graph).
        """
        # call nodes.remove (remove the node, returns true/false if successful/unsuccessful).
        flag = self.nodes.remove(label)
        # if the node was removed.
        if flag:
            # for each edge connected to the node with label 'label'.
            for edge in self.edges.get_edge_by_node(label).set:
                # call edges.remove (remove the edge).
                self.edges.remove(edge.uid)


    def remove_edge(self, uid):
        """
            A method of Graph.

            Parameter(s):
            -------------
            label : String
                The label of the edge to be removed.
            
            Returns:
            --------
            None, removes the corresponding edge.
        """
        self.edges.remove(uid)


    def get_node_connections(self, label):
        node = self.nodes.get(label)
        graph = self.__class__(label + '-Network')
        graph.edges = node.nodeof() # do this before updating node's graph.
        graph.nodes = node.neighbours()
        graph.add_node(label)
        for node in graph.nodes.set:
            node.graph = graph
        return graph


    def details(self):
        """
            A method of Graph.
            
            Returns:
            --------
            None, prints details about the graph's properties.
        """
        print("\n\tGraph Details: \n\tLabel: %s \n\tDirected: %s \n\tStatic: %s" %(self.label, self.directed, self.static))
        print("\t#Nodes: %s \n\t#Edges: %s \n" % (self.nodes.count(), self.edges.count()))


    def print(self):
        """
            A method of Graph.
            
            Returns:
            --------
            None, calls node.print() and edges.print().
        """
        self.nodes.print()
        print()
        self.edges.print()
        print()



class TemporalGraph(Graph):
    """
        A class which represents a static, undirected graph consisting of nodes and edges.

        Parameter(s):
        -------------
        label : String
            A label for the graph.
        data : Input
            A valid Input class/subclass.

        Object Propertie(s):
        --------------------
        label : String
            Inherited from Graph.
        directed : Boolean
            Inherited from Graph.
        static : Boolean
            Inherited from Graph.
        nodes : Nodes
            Inherited from Graph.
        edges : Edges
            An temporal edges collection representing all edges in the graph.

        See also:
        ---------
            Graph
            Digraph
            TemporalDiGraph
    """

    def __init__(self, label, data=None):
        super().__init__(label)
        self.static = False
        self.edges = TemporalEdges(self)

        # if input data is supplied.
        if data is not None:
            # build the graph using this data.
            self.build(data)


    def build(self, data):
        """
            A method of TemporalGraph.

            Parameter(s):
            -------------
            data : Input
                A valid Input class/subclass.

            Returns:
            --------
                None, adds edges & nodes to the graph.
        """
        # for each edge in data['edges'].
        for index, edge in data.data['edges'].items():
            # add the edge using the add_edge method.
            self.add_edge(edge['node1'], edge['node2'], edge['tstart'], edge['tend'])
         # for each node in data['nodes'].
        for index, node in data.data['nodes'].items():
            # add the node using the add_node method.
            self.add_node(node)


    def add_edge(self, node1, node2, tstart, tend=None):
        """
            A method of TemporalGraph.

            Parameter(s):
            -------------
            node1 : String
                The label of the node1 connection.
            node2 : String
                The label of the node2 connection.
            tstart : Integer
                The start time of the temporal edge.
            tend : Integer
                The end time of the temporal edge.

            Returns:
            --------
            edge : TemporalEdge
                The corresponding edge object.
        """
        return self.edges.add(node1, node2, self.nodes, tstart, tend)


    def get_snapshot(self, time):
        """
            A method of TemporalGraph.

            Parameter(s):
            -------------
            time : Integer
                The time to take the snapshot at.

            Returns:
            --------
            graph : Graph
                A static undirected graph snapshot at time 'time'.
        """
        # update graph label.
        label = self.label + ' [time: ' + str(time) + ']'
        # create static snapshot.
        graph = Graph(label)
        # for each edge that is active at time 'time'.
        for edge in self.edges.get_active_edges(time).set:
            # add the edge to the snapshot.
            graph.add_edge(edge.node1.label, edge.node2.label)
        # for each node in the graph.
        for node in self.nodes.set:
            # add the node to the snapshot.
            graph.add_node(node.label)
        # return the snapshot.
        return graph


    def get_temporal_subgraph(self, interval):
        """
            A method of TemporalGraph.

            Parameter(s):
            -------------
            time : Tuple/List
                The interval (start & end time pair).

            Returns:
            --------
            graph : TemporalGraph
                A temporal graph with timespan 'interval'.
        """
        # update graph label.
        label = self.label + ' [time: ' + str(interval) + ']'
        # create subgraph.
        graph = self.__class__(label)
        # add the edges collection whose duration is within 'interval'.
        graph.edges = self.edges.get_edge_by_interval(interval)
        # for each node in the graph.
        for node in self.nodes.set:
            # add the node to the subgraph.
            graph.add_node(node.label)
        # return the subgraph.
        return graph
