

import unittest

import PyMarkdownGen.PyMarkdownGen as md

class BlockquoteTests(unittest.TestCase):


    def test_block_quote(self):
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
    unittest.main()
