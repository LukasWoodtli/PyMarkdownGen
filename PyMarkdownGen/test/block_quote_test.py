"""This module contains the unit tests for
   the formatting of block quotes.

"""

import unittest

import PyMarkdownGen.PyMarkdownGen as md

class BlockquoteTests(unittest.TestCase):
    """The test case (fixture) for testing block quotes."""

    def test_block_quote(self):
        """Tests block quotes that contains a '>'
           on every line.

        """

        expected = \
"""> this is a
> block quote
> on multiple
> lines.
"""
        self.assertEqual(expected,
                         md.gen_block_quote(
                             "this is a\nblock quote\n"
                             "on multiple\r\nlines."))


    def test_block_quote_simple(self):
        """Tests block quotes that contain a '>'
           only on the first line.

        """

        expected = \
"""> this is a simple
block quote
on multiple
lines.
"""
        self.assertEqual(expected,
                         md.gen_block_quote(
                             "this is a simple\nblock quote\n"
                             "on multiple\nlines.", True))



if __name__ == '__main__':
    unittest.main()  # pragma: no branch
