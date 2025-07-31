import unittest
from linked_list import DisjointSetLinkedList
from linked_list_weighted import DisjointSetLinkedListWeighted


class TestDisjointLinkedList(unittest.TestCase):
    def test_make_and_find_test(self):
        dsl = DisjointSetLinkedList()
        dsl.make_set(5)
        self.assertEqual(dsl.find_set(5).value, 5)

    def test_union(self):
        dsl = DisjointSetLinkedList()
        dsl.make_set(1)
        dsl.make_set(2)
        dsl.union(1, 2)
        self.assertEqual(dsl.find_set(1), dsl.find_set(2))


class TestDisjointLinkedListWeighted(unittest.TestCase):
    def test_make_and_find_set(self):
        dsl = DisjointSetLinkedListWeighted()
        dsl.make_set(3)
        dsl.make_set(4)
        self.assertEqual(dsl.sizes[3], 1)
        self.assertNotEqual(dsl.find_set(3), dsl.find_set(4))

    def test_union(self):
        ds = DisjointSetLinkedListWeighted()
        ds.make_set(1)
        ds.make_set(2)
        ds.make_set(3)
        ds.union(1, 2)
        ds.union(3, 2)
        self.assertEqual(ds.find_set(1), ds.find_set(3))
        self.assertEqual(ds.sizes[1], 3)


if __name__ == '__main__':
    unittest.main()
