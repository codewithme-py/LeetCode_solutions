import pytest

from solutions.median_of_two_sorted_arrays_0004 import Solution


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([0, 0], [0, 0], 0.0),
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([1, 3], [2, 4, 5], 3.0),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5)
])

def test_solution(nums1: list[int], nums2: list[int], expected: float) -> None:
    sol = Solution()

    assert sol.findMedianSortedArrays(nums1, nums2) == expected
