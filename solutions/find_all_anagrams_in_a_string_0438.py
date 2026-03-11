from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Finds all the initial anagram indexes of the p line in the s line.
        An anagram is a permutation of the letters of the string p.
        For example, 'ab' and 'ba' are anagrams.
        The algorithm uses a sliding window of fixed size len(p)
        And a dictionary for counting characters in the current window
        and in the reference line p.
        This allows you to compare the window with p for O(1) (on average),
        reaching Total time O(n), where n is the length of the string s.
        """
        if len(p) > len(s):
            return []
        p_count, window_count, result = Counter(p), Counter(), []
        for i in range(len(s)):
            window_count[s[i]] += 1
            if i >= len(p):
                window_count[s[i - len(p)]] -= 1
                if window_count[s[i - len(p)]] == 0:
                    del window_count[s[i - len(p)]]
            if window_count == p_count:
                result.append(i - len(p) + 1)
        return result
