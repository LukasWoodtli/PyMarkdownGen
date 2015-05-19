"""This test file contains a test that implements one of the original
Markdown test.
"""

__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.PyMarkdownGen as md
import PyMarkdownGen.Document as doc

class BlockQuoteTest(unittest.TestCase):
    """Test for the original file with block quote."""


    def test_something(self):
        """Define a text and create a block quote from it."""

        expected_output_text = get_expected_markdown_text("Blockquotes with code blocks.text")


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

        self.assertEqual(expected_output_text, md_document.get_markdown_text())


    def test_nested_block_quotes(self):
        """Test for nested block quotes."""

        expected_output_text = get_expected_markdown_text("Nested blockquotes.text")

        text = "foo"
        text += md.gen_section()
        text += md.gen_block_quote("bar")
        text += "\n"
        text += "foo"

        md_doc = doc.Document()
        md_doc.add_block_quote(text)

        self.assertEqual(expected_output_text, md_doc.get_markdown_text())

    def test_list_in_block_quote(self):
        """Tests tidyness with list in block quote."""

        expected_output_text = get_expected_markdown_text("Tidyness.text")

        text = "A list within a blockquote:"
        text += md.gen_section()
        text += md.gen_un_ordered_list(["asterisk 1", "asterisk 2", "asterisk 3"])

        md_doc = doc.Document()
        md_doc.add_block_quote(text)


        self.assertEqual(expected_output_text, md_doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main() # pragma: no cover
