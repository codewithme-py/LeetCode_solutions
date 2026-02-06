import pytest

from solutions.longest_substring_without_repeating_characters_0003 import Solution


@pytest.mark.parametrize('args, expected', [
    ('abcabcbb', 3), ('bbbbb', 1), ('pwwkew', 3), ('', 0), ('a', 1),
    ('au', 2), ('dvdf', 3), ('tmmzuxt', 5), ('anviaj', 5), ('ohvhjdml', 6),
    ('qrsvbspk', 5), ('', 0), ('a', 1), ('au', 2), ('dvdf', 3),
    ('tmmzuxt', 5), ('anviaj', 5), ('ohvhjdml', 6), ('qrsvbspk', 5),
    ('', 0), ('a', 1), ('au', 2), ('dvdf', 3), ('tmmzuxt', 5),
    ('anviaj', 5), ('ohvhjdml', 6), ('qrsvbspk', 5),
])
def test_solution(args: str, expected: int) -> None:
    sol = Solution()
    assert sol.lengthOfLongestSubstring(args) == expected
