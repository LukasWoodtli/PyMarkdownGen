"""This module contains some tests from the original
Markdown test suite."""

__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.Document as md_doc

class TestAmpsAndAngles(unittest.TestCase):
    """Some tests from the original Markdown test cases."""

    def setUp(self):
        """Set up the file with the expected output."""

        self.expected_output_text = get_expected_markdown_text("Amps and angle encoding.text")


    def test_amps_and_ange_encoding(self):
        """Create a text that represents the expected file."""

        md_document = md_doc.Document()
        md_document.add_text("AT&T has an ampersand in their name.")
        md_document.add_section()
        md_document.add_text("AT&amp;T is another way to write it.")
        md_document.add_section()
        md_document.add_text("This & that.")
        md_document.add_section()
        md_document.add_text("4 < 5.")
        md_document.add_section()
        md_document.add_text("6 > 5.")
        md_document.add_section()

        md_document.add_text("Here\'s a ")
        md_document.add_reference("1", "http://example.com/?foo=1&bar=2", "link")
        md_document.add_text(" with an ampersand in the URL.")
        md_document.add_section()


        md_document.add_text("Here's a link with an ampersand in the link text: ")
        md_document.add_reference("2", "http://att.com/", "AT&T")
        md_document.add_section()

        md_document.add_text("Here's an inline ")
        md_document.add_link("/script?foo=1&bar=2", "link")
        md_document.add_section()

        md_document.add_text("Here's an inline ")
        md_document.add_link("</script?foo=1&bar=2>", "link")
        md_document.add_section()

        self.assertEqual(self.expected_output_text, md_document.get_markdown_text(True))

if __name__ == '__main__':
    unittest.main()   # pragma: no cover
