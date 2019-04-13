import leetcode
import unittest


class Tests(unittest.TestCase):
    def test_btree(self):
        self.assertEqual(
            leetcode.btree_to_list(leetcode.list_to_btree([1, 2, 3, None, None, 4, 5])),
            [1, 2, 3, None, None, 4, 5],
        )

    def test_btree02(self):
        self.assertEqual(
            leetcode.btree_to_list(leetcode.list_to_btree([1, None, 2, None, 3])),
            [1, None, 2, None, 3],
        )

    def test_btree02(self):
        self.assertEqual(
            leetcode.btree_to_list(leetcode.list_to_btree([1, 2, None, 3])),
            [1, 2, None, 3],
        )



unittest.main()
