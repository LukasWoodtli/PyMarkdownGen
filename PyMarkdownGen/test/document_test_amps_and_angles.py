__author__ = 'Boot'

import unittest
from PyMarkdownGen.test.document_test_base import DocumentTestBase
import PyMarkdownGen.Document as md_doc

class TestAmpsAndAngles(DocumentTestBase):
    def setUp(self):
        self.set_expected("Amps and angle encoding.text")

    def test_amps_and_ange_encoding(self):
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
