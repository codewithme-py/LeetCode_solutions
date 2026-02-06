class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert integer to Roman numeral.
        Uses greedy algorithm with predefined value-symbol pairs including
        subtractive forms (IV, IX, XL, XC, CD, CM).
        Args:
            num: Integer in [1, 3999]
        Returns:
            Roman numeral string
        """
        roman_pairs = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        result = []
        for value, symbol in roman_pairs:
            count, num = divmod(num, value)
            result.append(symbol * count)
        return ''.join(result)
