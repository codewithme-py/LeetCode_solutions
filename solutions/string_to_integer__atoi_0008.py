class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Skip leading spaces
        Check sign
        Convert digits
        Check overflow
        Return result
        """
        flag, sign, result = 0, 1, 0
        space, plus, minus = ' ', '+', '-'
        INT_MAX, INT_MIN, OVERFLOW = 2**31 - 1, -2**31, 7
        length = len(s)
        while flag < length and s[flag] == space:
            flag += 1
        if flag < length and (s[flag] == plus or s[flag] == minus):
            sign = -1 if s[flag] == minus else 1
            flag += 1
        while flag < length and s[flag].isdigit():
            digit = ord(s[flag]) - ord('0')
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > OVERFLOW):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            flag += 1
        return sign * result
