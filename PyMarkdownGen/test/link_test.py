"""This module contains the unit tests for link generation."""

__author__ = 'Boot'

import unittest
import PyMarkdownGen.PyMarkdownGen as md


class LinkTests(unittest.TestCase):
    """The test case (fixture for link tests."""


    def test_link(self):
        """Simple link generation where only the URL is provided."""

        expected = "www.example.com"
        self.assertEqual(expected, md.gen_link("www.example.com"))


    def test_link_with_text(self):
        """A link that displays a different text than the URL."""

        expected = "[This is a link.](www.example.com)"
        self.assertEqual(expected, md.gen_link("www.example.com", "This is a link."))


    def test_link_with_txt_and_alt_txt(self):
        """A link that displays a different text than the URL.
        And has an alternative text."""

        expected = '[This is a link.](www.example.com "Alternative text")'
        self.assertEqual(expected,
                         md.gen_link("www.example.com",
                                     "This is a link.",
                                     "Alternative text"))

    def test_image_link(self):
        """Test a link to an inmage."""

        expected = '![alt text](http://example.com/example.jpg "Text")'
        self.assertEqual(expected,
                         md.gen_image_link("http://example.com/example.jpg",
                                           "Text",
                                           "alt text"))

if __name__ == '__main__':
    unittest.main()   # pragma: no branch
