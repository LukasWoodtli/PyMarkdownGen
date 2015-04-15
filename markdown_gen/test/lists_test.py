
import unittest
import markdown_gen.MardownGen as md


class ListTest(unittest.TestCase):
    def test_ordered_list(self):
        expected = \
"""1. first
2. second
3. third
4. and so on
"""
        self.assertEqual(expected, md.gen_ordered_list(["first", "second", "third", "and so on"]))


    def test_un_ordered_list(self):
        expected = \
"""* one intem
* next item
* one more
* and so on
"""
        self.assertEqual(expected, md.gen_un_ordered_list(["one intem", "next item", "one more", "and so on"]))

if __name__ == '__main__':
    unittest.main()
