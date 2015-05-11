__author__ = 'Boot'

import unittest
import PyMarkdownGen.Document as md


class DocumentTest(unittest.TestCase):
    def test_document_generation(self):
        doc = md.Document("test_doc.md")
        doc.add_heading("Test", 1, True)

        self.assertEqual("Test\n====\n", doc.get_markdown_text())


if __name__ == '__main__':
    unittest.main()
