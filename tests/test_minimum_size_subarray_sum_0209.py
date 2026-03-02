import pytest

from solutions.minimum_size_subarray_sum_0209 import Solution


@pytest.mark.parametrize('target, nums, expected', [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (1, [1, 1, 1, 1, 1, 1, 1, 1], 1),
    (11, [1, 1, 1, 1, 1], 0)
])
def test_min_subarray_len(target: int, nums: list[int], expected: int) -> None:
    sol = Solution()
    assert sol.minSubArrayLen(target, nums) == expected
