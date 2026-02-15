import pytest

from solutions.reverse_integer_0007 import Solution


@pytest.mark.parametrize('args, expected', [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0),
    (-2147483648, 0),
    (1563847412, 0),
    (1463847412, 2147483641),
    (1463847412, 2147483641),
])
def test_solution(args, expected):
    sol = Solution()
    assert sol.reverse(args) == expected
