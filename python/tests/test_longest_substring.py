import unittest
from src.longest_substring import length_of_longest_substring


class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        s = 'abcabcbb'
        expected = 3

        self.assertEqual(length_of_longest_substring(s), expected)

    def test_length_of_longest_substring_empty(self):
        s = ''
        expected = 0

        self.assertEqual(length_of_longest_substring(s), expected)

    def test_length_of_longest_substring_not_moving_backwards(self):
        s='abba'
        expected = 2

        self.assertEqual(length_of_longest_substring(s), expected)


if __name__ == '__main__':
    unittest.main()