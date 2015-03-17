

import unittest

import markdown_gen.MardownGen as md

class AttributesTests(unittest.TestCase):


    def test_italic(self):
        expected = "*italic text*"
        self.assertEqual(expected, md.gen_italic("italic text"))

        expected = "_italic text alternative_"
        self.assertEqual(expected, md.gen_italic("italic text alternative", True))


    def test_bold(self):
        expected = "**bold text**"
        self.assertEqual(expected, md.gen_bold("bold text"))

        expected = "__bold text alternative__"
        self.assertEqual(expected, md.gen_bold("bold text alternative", True))
        
    def test_bold_and_italic(self):
        expected = "***bold and italic text***"
        self.assertEqual(expected, md.gen_italic(md.gen_bold("bold and italic text")))
        self.assertEqual(expected, md.gen_bold(md.gen_italic("bold and italic text")))

        expected =  "**asterisks and _underscores_**"

        self.assertEqual(expected, md.gen_bold("asterisks and " + md.gen_italic("underscores", True)))

    def test_monspace(self):
        expected = "`monospace`"
        self.assertEqual(expected, md.gen_monospace("monospace"))

    def test_strikethrough(self):
        expected = "~~strikethrough~~"
        self.assertEqual(expected, md.gen_strikethrough("strikethrough"))





if __name__ == '__main__':
    unittest.main()