

import unittest

import markdown_gen.MardownGen as md

class TestHeadingGenerator(unittest.TestCase):


    def test_heading_1(self):
        expected = "# Heading 1\n"
        self.assertEqual(expected, md.gen_heading("Heading 1", 1))

    def test_heading_2(self):
        expected = "## Heading 2\n"
        self.assertEqual(expected, md.gen_heading("Heading 2", 2))

    def test_heading_4(self):
        expected = "#### Heading 3\n"
        self.assertEqual(expected, md.gen_heading("Heading 3", 4))

    def test_heading_1_alternative(self):
        expected = "Heading 1\n" + \
                   "=========\n"
        self.assertEqual(expected, md.gen_heading("Heading 1", 1, True))

    def test_heading_2_alternative(self):
        expected = "Heading 2\n" + \
                   "---------\n"
        self.assertEqual(expected, md.gen_heading("Heading 2", 2, True))

    def test_heading_alternative(self):
        expected = "### Heading 3\n"
        self.assertEqual(expected, md.gen_heading("Heading 3", 3, True))





if __name__ == '__main__':
    unittest.main()