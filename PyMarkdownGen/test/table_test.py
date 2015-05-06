# coding=utf-8

import unittest

import PyMarkdownGen.PyMarkdownGen as md

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


    def test_table_alignment(self):
        expected = \
"""\
| Tables        |      Are      |  Cool |
|---------------|:-------------:|------:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      |   centered    |   $12 |
| zebra stripes |   are neat    |    $1 |
"""
        data = [["Tables", "Are", "Cool"],
                ["col 3 is", "right-aligned", "$1600"],
                ["col 2 is", "centered", "$12"],
                ["zebra stripes", "are neat", "$1"]]
        self.assertEqual(expected, md.gen_table(data, ['<', '^', '>']))

        # more than needed align chars
        self.assertEqual(expected, md.gen_table(data, ['<', '^', '>', '>']))

        expected = \
"""\
| Tables        |      Are      | Cool  |
|---------------|:-------------:|-------|
| col 3 is      | right-aligned | $1600 |
| col 2 is      |   centered    | $12   |
| zebra stripes |   are neat    | $1    |
"""
        # less than needed align chars: default is left aligned
        self.assertEqual(expected, md.gen_table(data, ['<', '^']))

if __name__ == '__main__':
    unittest.main()