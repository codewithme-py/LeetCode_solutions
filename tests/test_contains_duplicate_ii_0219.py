import pytest

from solutions.contains_duplicate_ii_0219 import Solution


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False),
    ([99,99], 2, True),
    ([1,2,3,4,5,6,7,8,9,10], 3, False),
])
def test_solution(nums: list[int], k: int, expected: bool) -> None:
    sol = Solution()
    assert sol.containsNearbyDuplicate(nums, k) == expected
