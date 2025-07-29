class ForestNode:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0  # For balanced union

class DisjointSetForest:
    def __init__(self):
        self.nodes = {}

    def make_set(self, x):
        if x not in self.nodes:
            self.nodes[x] = ForestNode(x)

    def find_set(self, x):
        node = self.nodes[x]
        if node.parent != node:
            node.parent = self.find_set(node.parent.value)  # Compression path
        return node.parent

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x == root_y:
            return

        # Union with rank
        if root_x.rank < root_y.rank:
            root_x.parent = root_y
        elif root_x.rank > root_y.rank:
            root_y.parent = root_x
        else:
            root_y.parent = root_x
            root_x.rank += 1
