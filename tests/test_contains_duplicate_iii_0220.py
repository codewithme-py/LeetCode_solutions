import pytest

from solutions.contains_duplicate_iii_0220 import Solution


@pytest.mark.parametrize(
    'nums, index_diff, value_diff, expected', [
        ([1,2,3,1], 3, 0, True),
        ([1,5,9,1,5,9], 2, 3, False),
    ]
)
def test_solution(nums, index_diff, value_diff, expected) -> None:
    sol = Solution()
    assert sol.containsNearbyAlmostDuplicate(nums, index_diff, value_diff) == expected
