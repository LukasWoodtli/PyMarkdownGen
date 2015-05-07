"""Unit tests for testing text attribues such as

- italics
- bold
- monospace
- strike trough

"""

import unittest

import PyMarkdownGen.PyMarkdownGen as md

class AttributesTests(unittest.TestCase):
    """The test case (fixture) for the attributes tests."""

    def test_italic(self):
        """Test italic text.

        The regular format (with '*') and the alternative
        format (with '_') is tested.

        """

        expected = "*italic text*"
        self.assertEqual(expected, md.gen_italic("italic text"))

        expected = "_italic text alternative_"
        self.assertEqual(expected, md.gen_italic("italic text alternative", True))


    def test_bold(self):
        """Test bold text.

        The regular format (with '*') and the alternative
        format (with '_') is tested.

        """

        expected = "**bold text**"
        self.assertEqual(expected, md.gen_bold("bold text"))

        expected = "__bold text alternative__"
        self.assertEqual(expected, md.gen_bold("bold text alternative", True))

    def test_bold_and_italic(self):
        """Test italic and bold text.

        The regular format (with '*') and the alternative
        format (with '_') is tested.
        Also the combination of the two formats is tested.

        """

        expected = "***bold and italic text***"
        self.assertEqual(expected, md.gen_italic(md.gen_bold("bold and italic text")))
        self.assertEqual(expected, md.gen_bold(md.gen_italic("bold and italic text")))

        expected = "**asterisks and _underscores_**"

        self.assertEqual(expected, md.gen_bold("asterisks and " +
                                               md.gen_italic("underscores", True)))

    def test_monspace(self):
        """Test text that should be typed in a monospace font."""

        expected = "`monospace`"
        self.assertEqual(expected, md.gen_monospace("monospace"))

    def test_strikethrough(self):
        """Test text that is striked through."""
        expected = "~~strikethrough~~"
        self.assertEqual(expected, md.gen_strikethrough("strikethrough"))





if __name__ == '__main__':
    unittest.main()
