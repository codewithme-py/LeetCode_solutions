import pytest

from solutions.sliding_window_maximum_0239 import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
    ([1], 1, [1]),
    ([1, -1], 1, [1, -1]),
    ([9, 11], 2, [11]),
    ([4, -2], 2, [4]),
])

def test_solution(nums: list[int], k: int, expected: list[int]) -> None:
    sol = Solution()
    assert sol.maxSlidingWindow(nums, k) == expected
