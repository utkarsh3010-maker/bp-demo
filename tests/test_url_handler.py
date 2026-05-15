import unittest
from utils.url_handler import normalize_url
from exceptions import URLValidationError

class TestURLHandler(unittest.TestCase):
    def test_standard_url(self):
        self.assertEqual(normalize_url("https://Example.Com/Path"), "https://example.com/Path")

    def test_missing_scheme(self):
        self.assertEqual(normalize_url("example.com"), "https://example.com")

    def test_whitespace_handling(self):
        self.assertEqual(normalize_url("  example.com  "), "https://example.com")

    def test_empty_string(self):
        with self.assertRaises(URLValidationError):
            normalize_url("   ")

    def test_invalid_structure(self):
        # Testing a case where netloc cannot be parsed correctly
        with self.assertRaises(URLValidationError):
            normalize_url("https://")

if __name__ == "__main__":
    unittest.main()
