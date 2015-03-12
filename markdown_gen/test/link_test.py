__author__ = 'Boot'

import unittest
import markdown_gen.MardownGen as md


class LinkTests(unittest.TestCase):
    def test_link(self):
        expected = "www.example.com\n"
        self.assertEqual(expected, md.gen_link("www.example.com"))

    def test_link_with_text(self):
        expected = "[This is a link.](www.example.com)\n"
        self.assertEqual(expected, md.gen_link("www.example.com", "This is a link."))

    def test_link_with_text_and_alternative_text(self):
        expected = '[This is a link.](www.example.com "Alternative text")\n'
        self.assertEqual(expected, md.gen_link("www.example.com", "This is a link.", "Alternative text"))

if __name__ == '__main__':
    unittest.main()
