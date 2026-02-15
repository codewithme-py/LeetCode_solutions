class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of an integer.
        Example 1:
        Input: x = 123
        Output: 321
        Example 2:
        Input: x = -123
        Output: -321
        Example 3:
        Input: x = 120
        Output: 21
        Note:
        Assume we are dealing with an environment which could only store
        integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
        For the purpose of this problem, assume that
        your function returns 0 when the reversed integer overflows.
        """
        int_min, int_max, reversed_num = -2**31, 2**31 - 1, 0
        sign = 1 if x >= 0 else -1
        x_abs = abs(x)
        while x_abs:
            digit = x_abs % 10
            reversed_num = reversed_num * 10 + digit
            if sign * reversed_num < int_min or sign * reversed_num > int_max:
                return 0
            x_abs //= 10
        return sign * reversed_num
