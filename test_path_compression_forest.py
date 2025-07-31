import unittest
from path_compression_forest import DisjointSetForest


class MyTestCase(unittest.TestCase):
    def test_make_and_find_sets(self):
        dsf = DisjointSetForest()
        dsf.make_set(1)
        dsf.make_set(2)
        self.assertNotEqual(dsf.find_set(1), dsf.find_set(2))

    def test_union(self):
        dsf = DisjointSetForest()
        dsf.make_set(1)
        dsf.make_set(2)
        dsf.make_set(3)
        dsf.union(1, 2)
        self.assertEqual(dsf.find_set(1), dsf.find_set(2))
        dsf.union(1, 3)
        self.assertEqual(dsf.find_set(1), dsf.find_set(3))

    def test_compression(self):
        dsf = DisjointSetForest()
        dsf.make_set(1)
        dsf.make_set(2)
        dsf.make_set(3)
        dsf.make_set(4)
        before = dsf.nodes[4].parent
        dsf.union(1, 2)
        dsf.union(2, 3)
        dsf.union(3, 4)
        after = dsf.nodes[4].parent
        self.assertNotEqual(before, after)
        self.assertEqual(dsf.find_set(4), after)


if __name__ == '__main__':
    unittest.main()
