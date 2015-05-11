"""This module contains some default tests for the
document based API.

"""

__author__ = 'Lukas Woodtli'

import unittest
import PyMarkdownGen.Document as md


class DocumentTest(unittest.TestCase):
    """The test case (fixture) for the document based tests."""


    def test_document_generation(self):
        """Tests a simple case of the document based API."""

        doc = md.Document("test_doc.md")
        doc.add_heading("Test", 1, True)

        self.assertEqual("Test\n====\n", doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
