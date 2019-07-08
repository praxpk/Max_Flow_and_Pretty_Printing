"""
Ford Fulkerson method referenced from https://en.wikipedia.org/wiki/Ford–Fulkerson_algorithm
"""
from node import node

class graph():
    __slots__ = 'vertices', 'edges','flow'

    def __init__(self):
        self.vertices = [] #contains the vertices of the graph
        # contains the edges of the graph as a dictionary.
        # The key of the dictionary is a tuple of the two vertices that make the edge
        # and the edge weight is its value
        self.edges = {}
        #this maintains the flow separately, increments or decrements the flow with each cycle.
        self.flow = {}


    def path_exists(self, start_vertex, end_vertex, path):
        """
        This returns true if there is a path between the source and the sink and returns
        the path that leads from the source to sink
        :param start_vertex: the source
        :param end_vertex: the vertex
        :param path: a dictionary that has a vertex as the key and the other vertex of the edge as value
        :return: returns true if the end vertex has been reached with the flow still left in the edges.
        """
        queue1 = list()
        visited = {}
        for i in self.vertices:
            visited[i]=False
        queue1.append(start_vertex)
        visited[start_vertex] = True
        while (len(queue1) != 0):
            aVertex = queue1.pop(0)
            for i in aVertex.get_neighbours().keys():
                if(visited[i]==False and self.flow[(aVertex,i)]>0):
                    queue1.append(i)
                    path[i] = aVertex
                    visited[i] = True

        return visited[end_vertex]

    def find_max_flow(self, source, sink):
        max_flow = 0
        path = {}
        while self.path_exists(source, sink, path) is not False:
            individual_flow = float("inf")
            aNode = sink
            while source != aNode:
                flow1 = individual_flow
                flow2 = self.flow[(path[aNode],aNode)]
                individual_flow = min(flow1, flow2)
                if(path.get(aNode) is not None):
                    aNode = path.get(aNode)

            max_flow += individual_flow

            aNode = sink
            bNode=0
            while aNode != source:
                if(path.get(aNode) is not None):
                    bNode = path.get(aNode)
                self.flow[(bNode, aNode)] -= individual_flow
                self.flow[(aNode, bNode)] += individual_flow
                if (path.get(aNode) is not None):
                    aNode = path.get(aNode)


        return max_flow

    def add_vertex(self, aVertex):
        self.vertices.append(aVertex)

    def add_edge(self, aVertex, bVertex, value):
        self.edges[(aVertex, bVertex)] = value
        self.flow[(aVertex, bVertex)] = value
        self.flow[(bVertex,aVertex)] = 0-value
        aVertex.add_neighbours(bVertex, value)
