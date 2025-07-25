class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.rep = self # Pointer to set representative

class DisjointLinkedList:
    def __init__(self):
        self.representatives = {}

    def make_set(self, x):
        node = Node(x)
        self.representatives[x] = node

    def find(self, x):
        return self.representatives[x].rep.value

    def union(self,x,y):
        rep_x = self.representatives[x].rep
        rep_y = self.representatives[y].rep

        if rep_x == rep_y:
            return
        current = rep_x
        while current.next:
            current = current.next
        current.next = rep_y

        current = rep_y
        while current:
            current.rep = rep_x
            current = current.next


