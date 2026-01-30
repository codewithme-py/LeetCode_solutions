from solutions.roman_to_integer_0013 import Solution


def test_roman_to_int():
    sol = Solution()
    assert sol.romanToInt('III') == 3
    assert sol.romanToInt('LVIII') == 58
    assert sol.romanToInt('MCMXCIV') == 1994
    assert sol.romanToInt('IV') == 4
    assert sol.romanToInt('IX') == 9
    assert sol.romanToInt('XL') == 40
    assert sol.romanToInt('XC') == 90
    assert sol.romanToInt('CD') == 400
    assert sol.romanToInt('CM') == 900
    assert sol.romanToInt('M') == 1000
