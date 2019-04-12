import leetcode
import unittest


class Tests(unittest.TestCase):
    def test_btree(self):
        self.assertEqual(
            leetcode.btree_to_list(leetcode.list_to_btree([1, 2, 3, None, None, 4, 5])),
            [1, 2, 3, None, None, 4, 5],
        )


unittest.main()
