__author__ = 'Boot'

import unittest
import markdown_gen.MardownGen as md


class LinkTests(unittest.TestCase):
    def test_link(self):
        expected = "www.example.com"
        self.assertEqual(expected, md.gen_link("www.example.com"))

    def test_link_with_text(self):
        expected = "[This is a link.](www.example.com)"
        self.assertEqual(expected, md.gen_link("www.example.com", "This is a link."))

    def test_link_with_text_and_alternative_text(self):
        expected = '[This is a link.](www.example.com "Alternative text")'
        self.assertEqual(expected, md.gen_link("www.example.com", "This is a link.", "Alternative text"))

    def test_image_link(self):
        expected = '![alt text](http://example.com/example.jpg "Text")'
        self.assertEqual(expected, md.gen_image_link("http://example.com/example.jpg", "Text", "alt text"))

if __name__ == '__main__':
    unittest.main()
