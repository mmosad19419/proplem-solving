import unittest
from src.merge_intervals import merge_intervals 

class TestMergeIntervals(unittest.TestCase):

    def test_regular_intervals(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_empty_input(self):
        self.assertEqual(merge_intervals([]), [])

    def test_single_interval(self):
        self.assertEqual(merge_intervals([[5,7]]), [[5,7]])

    def test_all_overlapping(self):
        intervals = [[1,4],[2,5],[3,6]]
        expected = [[1,6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_no_overlaps(self):
        intervals = [[1,2],[3,4],[5,6]]
        expected = [[1,2],[3,4],[5,6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_touching(self):
        intervals = [[1,2],[2,3],[3,4]]
        expected = [[1,4]]  # touching counts as overlapping
        self.assertEqual(merge_intervals(intervals), expected)

    def test_unsorted_input(self):
        intervals = [[5,6],[1,2],[3,4]]
        expected = [[1,2],[3,4],[5,6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_mixed_intervals(self):
        intervals = [[1,4],[0,0],[5,7],[6,8]]
        expected = [[0,0],[1,4],[5,8]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_intervals_with_negative_numbers(self):
        intervals = [[-5,-3],[-4,-2],[0,2],[1,3]]
        expected = [[-5,-2],[0,3]]
        self.assertEqual(merge_intervals(intervals), expected)

if __name__ == "__main__":
    unittest.main()
