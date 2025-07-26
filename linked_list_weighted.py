class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.rep = self # Pointer to set's representative

class DisjointSetLinkedListWeighted:
    def __init__(self):
        self.representatives = {}
        self.sizes = {}

    def make_set(self, x):
        node = Node(x)
        self.representatives[x] = node
        self.sizes[x] = 1

    def find_set(self,x):
        return self.representatives[x].rep

    def union(self,x,y):
        rep_x = self.representatives[x].rep
        rep_y = self.representatives[y].rep

        if rep_x == rep_y:
            return

        # Weighted Union Heuristic: append the short list to the long one
        if self.sizes[rep_x] < self.sizes[rep_y]:
            rep_x, rep_y = rep_y, rep_x # Swap

        current = rep_x
        while current.next:
            current = current.next
        current.next = rep_y

        current = rep_y
        while current:
            current.rep = rep_x
            current = current.next

        # Update size
        self.sizes[rep_x] += self.sizes[rep_y]
        del self.sizes[rep_y]



