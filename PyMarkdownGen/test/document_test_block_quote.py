"""This test file contains a test that implements one of the original
Markdown test.
"""

__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.Document as doc

class BlockQuoteTest(unittest.TestCase):
    """Test for the original file with block quote."""

    def setUp(self):
        """Set up the file with the expected output."""

        self.expected_output_text = get_expected_markdown_text("Blockquotes with code blocks.text")



    def test_something(self):
        """Define a text and create a block qote from it."""

        text = \
"""Example:

    sub status {
        print "working";
    }

Or:

    sub status {
        return "working";
    }
"""
        md_document = doc.Document()
        md_document.add_block_quote(text)

        self.assertEqual(self.expected_output_text, md_document.get_markdown_text())


if __name__ == '__main__':
    unittest.main()
