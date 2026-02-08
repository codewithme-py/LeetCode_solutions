class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in the given string.
        Args:
            s: The input string.
        Returns:
            The longest palindromic substring in the input string.
        """
        start = 0
        max_len = 1
        if len(s) <= 1:
            return s

        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1, left + 1

        for i in range(len(s)):
            length_odd, start_odd = expand_around_center(i, i)
            if length_odd > max_len:
                max_len = length_odd
                start = start_odd
            length_even, start_even = expand_around_center(i, i + 1)
            if length_even > max_len:
                max_len = length_even
                start = start_even
        return s[start:start + max_len]
