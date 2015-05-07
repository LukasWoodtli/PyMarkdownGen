"""This module contains the unit tests for list generation."""
import unittest
import PyMarkdownGen.PyMarkdownGen as md


class ListTest(unittest.TestCase):
    """The test case (fixture) for the tests for list generation."""

    def test_ordered_list(self):
        """Create a ordered (numbered) list."""

        expected = \
"""1. first
2. second
3. third
4. and so on
"""
        self.assertEqual(expected, md.gen_ordered_list(["first", "second", "third", "and so on"]))


    def test_un_ordered_list(self):
        """Create a unordered bullet list."""
        expected = \
"""* one intem
* next item
* one more
* and so on
"""
        self.assertEqual(expected, md.gen_un_ordered_list(
            ["one intem", "next item", "one more", "and so on"]))

if __name__ == '__main__':
    unittest.main()
