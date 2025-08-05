import unittest
from connected_components import *
from path_compression_forest import DisjointSetForest
from linked_list_weighted import DisjointSetLinkedListWeighted
from linked_list import DisjointSetLinkedList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.nodes = [0, 1, 2, 3, 4]
        self.edges = [(0, 1), (2, 3)]

    #  Three connected components

    def check_components(self, components, expected_result):
        self.assertEqual(len(components), expected_result)

    def test_linked_list(self):
        ll = DisjointSetLinkedList()
        components = connected_components(self.nodes, self.edges, ll)
        self.check_components(components, 3)

    def test_linked_list_weighted(self):
        llw = DisjointSetLinkedListWeighted()
        components = connected_components(self.nodes, self.edges, llw)
        self.check_components(components, 3)

    def test_path_compression_forest(self):
        pcf = DisjointSetForest()
        components = connected_components(self.nodes, self.edges, pcf)
        self.check_components(components, 3)


if __name__ == '__main__':
    unittest.main()
