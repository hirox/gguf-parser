"""Tests for gguf_parser.py"""

import unittest
from gguf_parser import GGUFParser, GGUFParseError


class TestGGUFParser(unittest.TestCase):
    def setUp(self):
        self.parser = GGUFParser("tests/dummy.gguf")

    def test_parse(self):
        try:
            self.parser.parse()
        except GGUFParseError as e:
            self.fail(f"GGUFParseError raised: {e}")

    def test_load_tensors(self):
        try:
            self.parser.parse()
            self.parser.load_tensors()
        except Exception as e:
            self.fail(f"Exception raised: {e}")


if __name__ == "__main__":
    unittest.main()
