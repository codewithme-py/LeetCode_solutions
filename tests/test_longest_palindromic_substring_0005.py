import pytest

from solutions.longest_palindromic_substring_0005 import Solution


@pytest.mark.parametrize('args, expected', [
    ('babad', 'bab'),
    ('cbbd', 'bb'),
    ('a', 'a'),
    ('ac', 'a')
])
def test_solution(args: str, expected: str) -> None:
    sol = Solution()
    assert sol.longestPalindrome(args) == expected
