

import unittest

import markdown_gen.MardownGen as md

class TestTableGenerator(unittest.TestCase):

    def setUp(self):
        self.data = [
            ["abcdefghij", "aaa", "b"],
            ["b", "c", "b"],
            ["dddddddddd", "a", "c"]
        ]

    def test_table_gen(self):
        expected = \
"""| abcdefghij | aaa | b |
|------------|-----|---|
| b          | c   | b |
| dddddddddd | a   | c |
"""

        self.assertEqual(expected, md.gen_table(self.data))


if __name__ == '__main__':
    unittest.main()