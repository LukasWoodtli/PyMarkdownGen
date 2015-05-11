"""This module contains common unit test functionality."""

__author__ = 'Lukas Woodtli'

import os


EXPECTED_OUTPUT_FOLDER = os.path.dirname(os.path.realpath(__file__))

def get_expected_markdown_text(expected_output_file):
    """Get the expected Markdown text from the given file.

    Args:
      expected_output_file (string): File name of the file with the expected
        Markdown text.

    """

    expected_path = os.path.join(EXPECTED_OUTPUT_FOLDER, "expected_output")
    expected_output_file = os.path.join(expected_path, expected_output_file)
    return file(expected_output_file).read()
