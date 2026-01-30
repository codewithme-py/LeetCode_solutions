class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Check if integer is a palindrome without string conversion.
        Negative numbers and trailing-zero numbers (except 0) are non-palindromic.
        Uses O(1) space by reversing half the number.
        Args:
            x: Integer in [-2^31, 2^31 - 1]
        Returns:
            True if x is palindrome, False otherwise
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10
        return x == reversed_half or x == reversed_half // 10
