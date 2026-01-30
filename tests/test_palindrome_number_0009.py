from solutions.palindrome_number_0009 import Solution


def test_is_palindrome():
    sol = Solution()
    assert sol.isPalindrome(121)
    assert not sol.isPalindrome(-121)
    assert not sol.isPalindrome(10)
    assert sol.isPalindrome(0)
    assert sol.isPalindrome(1221)
    assert sol.isPalindrome(12321)
    assert not sol.isPalindrome(123)
