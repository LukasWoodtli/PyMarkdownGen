"""Tis module contains the unit tests for generating headings."""

import unittest

import PyMarkdownGen.PyMarkdownGen as md

class HeadingTests(unittest.TestCase):
    """The test case (fixture) for generating headings."""

    def test_heading_1(self):
        """Test heading of depth 1. The default variant (with '#')."""

        expected = "# Heading 1\n"
        self.assertEqual(expected, md.gen_heading("Heading 1", 1))


    def test_heading_2(self):
        """Test heading of depth 2. The default variant (with '##')."""

        expected = "## Heading 2\n"
        self.assertEqual(expected, md.gen_heading("Heading 2", 2))


    def test_heading_4(self):
        """Test heading of depth 4. The default variant (with '####')."""
        expected = "#### Heading 3\n"
        self.assertEqual(expected, md.gen_heading("Heading 3", 4))


    def test_heading_1_alternative(self):
        """Test heading of depth 1. The default alternative variant (with '=')"""

        expected = "Heading 1\n" + \
                   "=========\n"
        self.assertEqual(expected, md.gen_heading("Heading 1", 1, True))


    def test_heading_2_alternative(self):
        """Test heading of depth 2. The alternative variant (with '-')"""
        expected = "Heading 2\n" + \
                   "---------\n"
        self.assertEqual(expected, md.gen_heading("Heading 2", 2, True))


    def test_heading_alternative(self):
        """Test heading of depth 3. The default variant (with '#') is forced."""
        expected = "### Heading 3\n"
        self.assertEqual(expected, md.gen_heading("Heading 3", 3, True))

    def test_new_line(self):
        """Tests the generation of a new line."""
        expected = "First line  \nnew line."
        actual = "First line"
        actual += md.gen_new_line()
        actual += "new line."
        self.assertEqual(expected, actual)

    def test_gen_section(self):
        """Test the generation of a new section."""
        expected ="Section 1\n\nSection 2"
        actual = "Section 1"
        actual += md.gen_section()
        actual += "Section 2"
        self.assertEqual(expected,actual)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
