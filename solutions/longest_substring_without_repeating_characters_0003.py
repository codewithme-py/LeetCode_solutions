class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left_border, max_len = 0, 0
        actual_set = set()
        for right_border, char in enumerate(s):
            while char in actual_set:
                actual_set.remove(s[left_border])
                left_border += 1
            actual_set.add(char)
            max_len = max(max_len, right_border - left_border + 1)
        return max_len
