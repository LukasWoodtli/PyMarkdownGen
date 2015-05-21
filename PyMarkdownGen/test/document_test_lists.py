"""This module tests ordered and unordered lists."""

__author__ = 'Lukas Woodtli'

import unittest
from PyMarkdownGen.test.document_test_common import get_expected_markdown_text
import PyMarkdownGen.Document as doc


class TestLists(unittest.TestCase):
    """Test case for testing lists."""
    def test_lists_eneration(self):
        """Tests the generation of ordered and unordered lists."""
        expected_output_text = get_expected_markdown_text("Ordered and unordered lists.text")

        md_doc = doc.Document()
        md_doc.add_heading("Unordered", 2)
        md_doc.add_text("\n")

        md_doc.add_text("Asterisks tight:")
        md_doc.add_section()

        md_doc.add_un_ordered_list(["asterisk 1", "asterisk 2", "asterisk 3"])
        md_doc.add_section()

        md_doc.add_text("* * *")
        md_doc.add_section()

        md_doc.add_text("Pluses tight:")
        md_doc.add_section()
        md_doc.add_un_ordered_list(["Plus 1", "Plus 2", "Plus 3"], '+')
        md_doc.add_section()

        md_doc.add_text("Minuses tight:")
        md_doc.add_section()

        md_doc.add_un_ordered_list(["Minus 1", "Minus 2", "Minus 3"], '-')
        md_doc.add_section()

        md_doc.add_heading("Ordered", 2)
        md_doc.add_text("\n")
        md_doc.add_text("Tight:")
        md_doc.add_section()

        md_doc.add_ordered_list(["One", "Two", "Three"])
        md_doc.add_section()


        self.assertEqual(expected_output_text, md_doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main() # pragma: no cover
