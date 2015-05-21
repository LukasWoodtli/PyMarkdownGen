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

        doc = md.Document()
        doc.add_heading("Test", 1, True)

        self.assertEqual("Test\n====\n", doc.get_markdown_text())

    def test_gen_new_line(self):
        """Tests a simple case for generating a new line."""

        doc = md.Document()
        doc.add_heading("Test", 1, True)
        doc.add_text("blabla")
        doc.add_new_line()

        self.assertEqual("Test\n====\nblabla  \n", doc.get_markdown_text())

    def test_gen_ordered_list(self):
        """Tests a simple case for generating a ordered list."""

        doc = md.Document()
        doc.add_heading("Test", 1, True)
        doc.add_ordered_list(["one", "two", "three"])


        self.assertEqual("Test\n====\n1. one\n2. two\n3. three\n", doc.get_markdown_text())


    def test_gen_block_quote(self):
        """Tests a simple case for generating a block quote."""

        doc = md.Document()
        doc.add_block_quote("one\ntwo\nthree")

        self.assertEqual("> one\n> two\n> three\n", doc.get_markdown_text())

        doc = md.Document()
        doc.add_block_quote("one\ntwo\nthree", True)

        self.assertEqual("> one\ntwo\nthree\n", doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main()   # pragma: no cover
