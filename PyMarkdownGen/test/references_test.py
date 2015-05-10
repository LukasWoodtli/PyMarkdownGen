"""This module contains the unit tests for generation of in-file references."""
import unittest

import PyMarkdownGen.PyMarkdownGen as md

class ReferencesTest(unittest.TestCase):
    """The test case (fixture) for reference generation."""


    def test_references_complex(self):
        """Test different possible styles of reference generation.

        The text is taken from:
        https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links

        """

        expected = \
"""[I'm a reference-style link][arbitrary reference text]

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself]

Some text to show that the reference links can follow later.

[arbitrary reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com
"""

        refs = []
        actual = ""
        txt, refs = md.gen_reference("arbitrary reference text",
                                     "https://www.mozilla.org",
                                     "I'm a reference-style link",
                                     refs)

        actual += txt + md.gen_section()
        txt, refs = md.gen_reference("1",
                                     "http://slashdot.org",
                                     "You can use numbers for reference-style link definitions",
                                     refs)

        actual += txt + md.gen_section()

        actual += "Or leave it empty and use the"
        txt, refs = md.gen_reference("link text itself",
                                     "http://www.reddit.com",
                                     references_list=refs)

        actual += txt + md.gen_section()
        actual += "Some text to show that the reference links can follow later." + md.gen_section()

        for reference in refs:
            actual += reference
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
