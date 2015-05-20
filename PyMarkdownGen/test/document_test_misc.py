"""This module tests some smaller features."""
__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.Document as doc

class TestMisc(unittest.TestCase):
    """Miscellaneous tests."""

    def test_html_comments(self):
        """Test the generation of HTML comments."""

        expected_output_text = get_expected_markdown_text("Inline HTML comments.text")

        md_doc = doc.Document()
        md_doc.add_text("Paragraph one.")
        md_doc.add_section()

        md_doc.add_html_comments("This is a simple comment")
        md_doc.add_section()

        md_doc.add_html_comments("\n\tThis is another comment.\n")
        md_doc.add_section()

        md_doc.add_text("Paragraph two.")
        md_doc.add_section()

        md_doc.add_html_comments("one comment block -- -- with two comments")
        md_doc.add_section()

        md_doc.add_text("The end.\n")

        self.assertEqual(expected_output_text, md_doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main() # pragma: no cover
