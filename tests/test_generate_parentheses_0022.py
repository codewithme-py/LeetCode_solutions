import pytest

from solutions.generate_parentheses_0022 import Solution


@pytest.mark.parametrize('n, expected', [
    (1, ['()']),
    (2, ['(())', '()()']),
    (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
])
def test_solution(n: int, expected: list[str]) -> None:
    sol = Solution()
    assert sol.generateParenthesis(n) == expected
