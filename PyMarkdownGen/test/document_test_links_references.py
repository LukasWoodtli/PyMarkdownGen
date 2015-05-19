"""Tests links and references against some of the original
Markdown test files."""

__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.PyMarkdownGen as md
import PyMarkdownGen.Document as doc

class LinkAndReferencesTest(unittest.TestCase):
    """Test cases for link and references generation."""

    def test_links_inline(self):
        """Test generation of links."""
        expected_output_text = get_expected_markdown_text("Links, inline style.text")

        md_doc = doc.Document()
        md_doc.add_text("Just a ")
        md_doc.add_link("/url/", "URL")
        md_doc.add_section()

        md_doc.add_link("/url/", "URL and title", "title")
        md_doc.add_section()

        md_doc.add_link("/url/ ", "URL and title", "title preceded by two spaces")
        md_doc.add_section()

        md_doc.add_link("/url/\t", "URL and title", "title preceded by a tab")
        md_doc.add_section()

        md_doc.add_link("", "Empty")
        md_doc.add_section()

        self.assertEqual(expected_output_text, md_doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main()
