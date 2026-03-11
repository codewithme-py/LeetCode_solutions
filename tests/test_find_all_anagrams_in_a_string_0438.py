import pytest

from solutions.find_all_anagrams_in_a_string_0438 import Solution


@pytest.mark.parametrize('s, p, expected', [
    ('cbaebabacd', 'abc', [0, 6]),
    ('abab', 'ab', [0, 1, 2]),
    ('ab', 'ab', [0]),
])
def test_solution(s: str, p: str, expected: list[int]) -> None:
    sol = Solution()
    assert sol.findAnagrams(s, p) == expected
