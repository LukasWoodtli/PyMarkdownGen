__author__ = 'Boot'
import os
import unittest

EXPECTED_OUTPUT_FOLDER = os.path.dirname(os.path.realpath(__file__))

class DocumentTestBase(unittest.TestCase):

    def set_expected(self, expected_output_file):
        expected_path = os.path.join(EXPECTED_OUTPUT_FOLDER, "expected_output")
        expected_output_file = os.path.join(expected_path, expected_output_file)
        self.expected_output_text = file(expected_output_file).read()
