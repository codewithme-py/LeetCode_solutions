from solutions.longest_common_prefix_0014 import Solution


def test_longest_common_prefix():
    sol = Solution()
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert sol.longestCommonPrefix([]) == ""
    assert sol.longestCommonPrefix(["hello"]) == "hello"
    assert sol.longestCommonPrefix(["test", "test", "test"]) == "test"
    assert sol.longestCommonPrefix(["a", "b"]) == ""
    assert sol.longestCommonPrefix(["", "abc"]) == ""
