from solutions.palindrome_number_0009 import Solution

def test_is_palindrome():
    sol = Solution()
    assert sol.isPalindrome(121) == True
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindrome(10) == False
    assert sol.isPalindrome(0) == True
    assert sol.isPalindrome(1221) == True
    assert sol.isPalindrome(12321) == True
    assert sol.isPalindrome(123) == False