class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert Roman numeral to integer.
        Handles subtractive notation (e.g. IV=4, IX=9).
        Assumes valid input per LeetCode constraints.
        Args:
            s: Roman numeral string (I, V, X, L, C, D, M)
        Returns:
            Integer value (1 to 3999)
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                total += roman_values[s[i]]
        return total
