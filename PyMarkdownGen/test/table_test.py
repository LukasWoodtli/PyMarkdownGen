# coding=utf-8
"""This module contains the unit tests for table generation."""
import unittest

import PyMarkdownGen.PyMarkdownGen as md

class TableTest(unittest.TestCase):
    """The test case (fixture) for table generation."""


    def test_table_gen(self):
        """Generate a table."""

        expected = \
"""\
| abcdefghij | aaa | b |
|------------|-----|---|
| b          | c   | b |
| dddddddddd | a   | c |
"""

        data = [
            ["abcdefghij", "aaa", "b"],
            ["b", "c", "b"],
            ["dddddddddd", "a", "c"]
            ]

        self.assertEqual(expected, md.gen_table(data))


    def test_table_alignment(self):
        """Generate a table that has different aligned columns."""

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
