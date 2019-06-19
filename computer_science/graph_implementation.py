"""
Complex Data Structures
Graph implementation in Python3
"""

class Vertex:

    def __init__(self, data):
        self.data = data

        # will be used to keep track of vertices linked with current vertex paired with their weight
        self.adjacents = {}

    def __str__(self):
        return "A vertex with data {}".format(self.data)

    # add a connection between two vertices. If a weight of connection is not passed, it defaults to 0
    def add_edge(self, vertex, weight=0):
        self.adjacents[vertex] = weight


class Graph:

    # when instantiating a graph, if nothing is declared, it defaults to a not directed graph. Anything that doesn't convert to False can be passed to change this behaviour; e.g. passing ````"directed"``` 
    # will do the job`
    def __init__(self, directed=False):
        # to keep track of vertices will e used a dictionary beacuse it can handle with ease the automatic instantiation of new Vertex objects
        self.vertices = {}
        self.directed = directed

    # add vertex to the graph. If the argument is not a Vertex instance, it is instantiated.
    def add_vertex(self, vertex):
        if type(vertex) == Vertex:
            self.vertices[vertex.data] = vertex
        else:
            self.vertices[vertex] = Vertex(vertex)

    #helper method to check if the argument passed is a Vertex instance. If not, return the Vertex instance associated
    def vertexize(self, to_check):
        if type(to_check) != Vertex:
            to_check = self.vertices[to_check]
        return to_check


    # add an edge between two vertices. If the graph is directed, the connection is not created in both direction but only in the direction that is passed as argument
    # It share interface with Vertex .add_edge() method, so give a glance to it to understand how it works.
    def add_edge(self, from_vertex, to_vertex, weight=0):
        from_vertex = self.vertexize(from_vertex)
        to_vertex = self.vertexize(to_vertex)
        from_vertex.add_edge(to_vertex, weight)
        if self.directed is False:
            to_vertex.add_edge(from_vertex, weight)
    
    #check whether exists a path between two vertices
    def exist_path(self, from_vertex, to_vertex):
        from_vertex = self.vertexize(from_vertex)
        to_vertex = self.vertexize(to_vertex)
        checked = []
        to_check = [from_vertex]
        while to_check:
            #we want to check from the start of the list because we want to search nearest vertices first, then move farther
            current_vertex = to_check.pop(0)
            checked.append(current_vertex)
            if current_vertex == to_vertex:
                return True
            to_check += [key for key in current_vertex.adjacents if key not in checked and key not in to_check]
        return False