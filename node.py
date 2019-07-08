class node():
    __slots__ = 'children', 'visited', 'name', 'parents'

    def __init__(self, value):
        self.name = value
        self.visited = False
        self.children = {}
        self.parents = {}

    def add_neighbours(self, aNeighbour,value):
        self.children[aNeighbour]=value
        aNeighbour.add_parent(self.name,value)

    def set_visited(self,bool1):
        self.visited = bool1

    def get_visited(self):
        return self.visited

    def get_neighbours(self):
        return self.children

    def get_this_neighbour(self,aNeighbour):
        if self.children.get(aNeighbour) is not None:
            return self.children[aNeighbour]
        else:
            return None

    def get_this_parent(self,aParent):
        if self.parents.get(aParent) is not None:
            return self.parents[aParent]
        else:
            return None

    def add_parent(self,aNode,value):
        self.parents[aNode]=value

    def get_parent(self):
        return self.parents

    def __str__(self):
        return str(self.name)