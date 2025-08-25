class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.rep = self  # Pointer to set's representative

class DisjointSetLinkedList:
    def __init__(self):
        self.representatives = {}

    def make_set(self, x):
        node = Node(x)
        self.representatives[x] = node

    def find_set(self, x):
        return self.representatives[x].rep

    def union(self,x,y):
        rep_x = self.representatives[x].rep
        rep_y = self.representatives[y].rep

        if rep_x == rep_y:
            return  # Already in the same set

        current = rep_x
        while current.next:
            current = current.next
        current.next = rep_y

        # Update the representative for y's node
        current = rep_y
        while current:
            current.rep = rep_x
            current = current.next


