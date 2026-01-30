from solutions.integer_to_roman_0012 import Solution


def test_int_to_roman():
    sol = Solution()
    assert sol.intToRoman(3749) == "MMMDCCXLIX"
    assert sol.intToRoman(58) == "LVIII"
    assert sol.intToRoman(1994) == "MCMXCIV"
    assert sol.intToRoman(1) == "I"
    assert sol.intToRoman(4) == "IV"
    assert sol.intToRoman(9) == "IX"
    assert sol.intToRoman(40) == "XL"
    assert sol.intToRoman(90) == "XC"
    assert sol.intToRoman(400) == "CD"
    assert sol.intToRoman(900) == "CM"
    assert sol.intToRoman(3999) == "MMMCMXCIX"
