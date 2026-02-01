import unittest
from src.merge_sorted_arrays import merge_sorted_arrays

class TestMergeSortedArrays(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        m = 3
        n = 3
        expected = [1, 2, 2, 3, 5, 6]
        result = merge_sorted_arrays(nums1, nums2, m, n)
        self.assertEqual(result, expected)

    def test_merge_sorted_arrays_empty_nums2(self):
        nums1 = [1]
        nums2 = []
        m = 1
        n = 0
        expected = [1]
        result = merge_sorted_arrays(nums1, nums2, m, n)
        self.assertEqual(result, expected)

    def test_merge_sorted_arrays_empty_nums1(self):
        nums1 = [0]
        nums2 = [1]
        m = 0
        n = 1
        expected = [1]
        result = merge_sorted_arrays(nums1, nums2, m, n)
        self.assertEqual(result, expected)

    def test_merge_sorted_arrays_both_empty(self):
        nums1 = []
        nums2 = []
        m = 0
        n = 0
        expected = []
        result = merge_sorted_arrays(nums1, nums2, m, n)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
