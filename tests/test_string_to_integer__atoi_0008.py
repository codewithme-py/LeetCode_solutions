import pytest

from solutions.string_to_integer__atoi_0008 import Solution


@pytest.mark.parametrize('args, expected', [
    ('42', 42),
    ('   -042', -42),
    ('1337c0d3', 1337),
    ('0-1', 0),
    ('words and 987', 0),
    ('-91283472332', -2147483648),
    ('2147483648', 2147483647),
    ('+-12', 0),
    ('  +  413', 0),
    ('4193 with words', 4193),
    ('91283472332', 2147483647)
])
def test_solution(args: str, expected: int) -> None:
    sol = Solution()
    assert sol.myAtoi(args) == expected
