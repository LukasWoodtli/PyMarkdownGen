# coding=utf-8

import unittest

import PyMarkdownGen.PyMardownGen as md

class TableTest(unittest.TestCase):

    def setUp(self):
        self.data = [
            ["abcdefghij", "aaa", "b"],
            ["b", "c", "b"],
            ["dddddddddd", "a", "c"]
        ]

    def test_table_gen(self):
        expected = \
"""\
| abcdefghij | aaa | b |
|------------|-----|---|
| b          | c   | b |
| dddddddddd | a   | c |
"""
        self.assertEqual(expected, md.gen_table(self.data))




if __name__ == '__main__':
    unittest.main()