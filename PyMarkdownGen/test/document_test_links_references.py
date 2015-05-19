"""Tests links and references against some of the original
Markdown test files."""

__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
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

    def test_quotes_in_link_titles(self):
        """Tests for quotes in link titles"""

        expected_output_text = get_expected_markdown_text("Literal quotes in titles.text")

        md_doc = doc.Document()
        md_doc.add_text("Foo ")
        md_doc.add_reference("", '/url/ "Title with "quotes" inside"', "bar")
        md_doc.add_section()

        md_doc.add_text("Foo ")
        md_doc.add_link("/url/", "bar", 'Title with "quotes" inside')
        md_doc.add_section()

        self.assertEqual(expected_output_text, md_doc.get_markdown_text())

    def test_references(self):
        """Tests for in file references"""

        expected_output_text = get_expected_markdown_text("Links, reference style.text")

        md_doc = doc.Document()

        md_doc.add_text("Foo ")
        md_doc.add_reference("1", '/url/  "Title"', "bar")
        md_doc.add_section()

        md_doc.add_references_list()
        md_doc.add_section()

        md_doc.add_text("Indented ")
        md_doc.add_reference("", "/url", "once")
        md_doc.add_section()

        md_doc.add_text("Indented ")
        md_doc.add_reference("", "/url", "twice")
        md_doc.add_section()

        md_doc.add_text("Indented ")
        md_doc.add_reference("", "/url", "thrice")
        md_doc.add_section()

        md_doc.add_text("Indented ")
        md_doc.add_reference("", "/url", "four")
        md_doc.add_text(" times.")
        md_doc.add_section()

        for i, ref in enumerate(md_doc.references_list):
            ref_text = " " * (i + 1)
            ref_text += ref + "\n"
            md_doc.add_text(ref_text)
        md_doc.references_list = [] # we need to clear the list here for further use


        md_doc.add_text("With ")
        md_doc.add_reference("b", "/url/", "embedded [brackets]")
        md_doc.add_section()
        md_doc.add_references_list()

        self.assertEqual(expected_output_text, md_doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main()
