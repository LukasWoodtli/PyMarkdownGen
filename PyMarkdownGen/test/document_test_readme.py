# coding=utf-8
"""This module tests the generation of an readme file.

As an example is the actual readme file taken. But it's
a copy since the original might change in the feature.

"""

__author__ = 'Lukas Woodtli'


import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.Document as md_doc

class TestReadmeGen(unittest.TestCase):
    """Some tests for generating a readme file."""

    def setUp(self):
        """Set up the file with the expected output."""

        self.expected_output_text = get_expected_markdown_text("expected_readme.text")


    def test_readme_gen(self):
        """Tests the generation of the readme with the OOP API."""

        md_document = md_doc.Document()
        md_document.add_heading("Markdown Generator for Python", alternative=True)

        md_document.add_heading("Status", 2, True)

        md_document.add_image_link(
            "https://travis-ci.org/LukasWoodtli/PyMarkdownGen.svg?branch=master",
            "Build Status",
            "Travis CI Build Status")

        md_document.add_section()

        md_document.add_heading("Objective", 2, True)

        md_document.add_text("This is a small Python library that helps generating ")
        md_document.add_link("http://en.wikipedia.org/wiki/Markdown", "Markdown")
        md_document.add_text(" documents.")

        md_document.add_section()

        md_document.add_heading("Examples", 2, True)
        md_document.add_heading("Text Attributes", 3)
        md_document.add_text("Text can be formatted with the attributes ")
        md_document.add_italic("italc")
        md_document.add_text(" and ")
        md_document.add_bold("bold")
        md_document.add_text(".\n")
        md_document.add_text("There is also ")
        md_document.add_monospace("monospace text")
        md_document.add_text(" or ")
        md_document.add_strikethrough("striketrough")
        md_document.add_text(".")

        md_document.add_section()

        md_document.add_heading("Features", 2, True)

        table_data = [["Feature", "Implemented", "Tested"],
                      ["Headers", "✓", "✓"],
                      ["Links", "✓", "✓"],
                      ["References", "✓", "✓"],
                      ["Images", "✓", "✓"],
                      ["Tables", "✓", "✓"],
                      ["Lists", "✓", "✓"],
                      ["Nested Lists", "✗", "✗"],
                      ["Blockquotes", "✓", "✓"],
                      ["Emphasis", "✓", "✓"],
                      ["Code and Syntax", "✗", "✗"]]

        md_document.add_table(table_data, ["<", "^", "^"])

        md_document.add_section()

        md_document.add_heading("To Do's", 2, True)

        md_document.add_un_ordered_list(["Docstrings",
                                         "Document based API (OOP)",
                                         "Documentation (ReadTheDocs)",
                                         "More unit tests"])

        md_document.add_section()

        md_document.add_heading("Further Notes", 2, True)
        md_document.add_text("...")



        self.assertEqual(self.expected_output_text, md_document.get_markdown_text(False))

if __name__ == '__main__':
    unittest.main()   # pragma: no cover
