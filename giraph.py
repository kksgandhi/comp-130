from collections import defaultdict
# from collections import set


class Graph1:

    """
    Directed graph stored as an adjacency list.
    A graph is a dictionary mapping nodes to sets of neighbors.
    A node can be of any immutable type.
    """

    def __init__(self):
        """Create an empty graph."""
        self.main_dictionary = defaultdict(set)

    def __str__(self):
        """
        Returns a printable string version of the graph
        in the form
        Graph(set([...]), set([...]))
        where the node set is printed first, then the
        edge set.
        """
        built_string = "Graph("
        built_string += str(self.get_nodes())
        built_string += ", "
        built_string += str(self.get_edges())
        built_string += ")"
        return built_string

    def add_node(self, name):
        """
        Adds the named node to the graph, if it doesn't already exist.
        Returns nothing.
        """
        if not name in self.main_dictionary:
            self.main_dictionary[name] = set()

    def add_edge(self, name_from, name_to):
        """
        Adds an edge from/to the named nodes, if it doesn't already exist.
        Also adds each of the named nodes, if they don't exist.
        Returns nothing.
        """
        self.add_node(name_from)
        self.add_node(name_to)
        self.main_dictionary[name_from].add(name_to)

    def get_nodes(self):
        """Returns a set of all the node names."""
        return_set = set()
        for key in self.main_dictionary:
            return_set.add(key)
        return return_set

    def get_node_neighbors(self, name_from):
        """
        Returns a set of all the named node's neighbors.
        The neighbors are those nodes that this node has an edge to.
        Returns an empty set if the node doesn't exist.
        """
        return self.main_dictionary[name_from]

    def get_edges(self):
        """
        Returns a set of all the edges.
        Each edge is a pair (tuple) of its source node,
        where it comes from, and its destination node,
        where it goes to.
        """
        return_set = set()
        for key in self.main_dictionary:
            for element in self.main_dictionary[key]:
                return_set.add((key, element))
        return return_set

    def is_neighbor(self, name_from, name_to):
        """
        Returns whether the named destination node is
        a neighbor of the named source node.
        """
        return name_to in self.main_dictionary[name_from]


class Graph2:

    def __init__(self):
        self._adjmatrix = []
        self._name = []

    def __str__(self):
        built_string = "Graph("
        built_string += str(self.get_nodes())
        built_string += ", "
        built_string += str(self.get_edges())
        built_string += ")"
        return built_string

    def add_node(self, name):
        if name not in self._name:
            self._name.append(name)
        while(len(self._name) > len(self._adjmatrix)):
            self._adjmatrix.append([])
        for single_list in self._adjmatrix:
            while(len(self._name) > len(single_list)):
                single_list.append(False)

    def add_edge(self, name_from, name_to):
        self.add_node(name_from)
        self.add_node(name_to)
        from_index = self._name.index(name_from)
        to_index = self._name.index(name_to)
        self._adjmatrix[from_index][to_index] = True

    def get_nodes(self):
        return_set = set()
        for value in self._name:
            return_set.add(value)
        return return_set

    def get_edges(self):
        return_set = set()
        for outer_index, outer_list in enumerate(self._adjmatrix):
            for inner_index, inner_item in enumerate(outer_list):
                if(inner_item):
                    return_set.add(
                        (self._name[outer_index],
                         self._name[inner_index]))
        return return_set

    def is_neighbor(self, name_from, name_to):
        from_index = self._name.index(name_from)
        to_index = self._name.index(name_to)
        return self._adjmatrix[from_index][to_index]

    def get_node_neighbors(self, node):
        return_set = set()
        for index, element in enumerate(self._adjmatrix[self._name.index(node)]):
            if element:
                return_set.add(self._name[index])
        return return_set


def is_partition(graph, nodeset1, nodeset2):
    if len(nodeset1) < 1:
        return False
    if len(nodeset2) < 1:
        return False
    if(len(nodeset1.intersection(nodeset2)) > 0):
        return False
    return_list = []
    return_list2 = []
    for element in nodeset1:
        return_list.append(element)
    for element in nodeset2:
        return_list2.append(element)
    index = 0
    while index < len(return_list):
        for element in graph.get_node_neighbors(return_list[index]):
            if element not in return_list:
                return_list.append(element)
        index += 1
    index = 0
    while index < len(return_list2):
        for element in graph.get_node_neighbors(return_list2[index]):
            if element not in return_list2:
                return_list2.append(element)
        index += 1
    return len(set(return_list).intersection(set(return_list2))) < 1


def connect_all(graph, nodeset):
    for element in nodeset:
        graph.add_node(element)
    for element1 in nodeset:
        for element2 in nodeset:
            if not element1 == element2:
                graph.add_edge(element1, element2)
    return graph


def shortest_path(graph, source, target):
    pass
