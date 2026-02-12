import pytest

from solutions.zigzag_conversion_0006 import Solution


@pytest.mark.parametrize('s, num_rows, expected', [
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ('A', 1, 'A'),
])
def test_solution(s: str, num_rows: int, expected: str) -> None:
    sol = Solution()
    assert sol.convert(s, num_rows) == expected
