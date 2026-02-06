class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Find the longest common prefix string
        amongst an array of strings.
        """
        if not strs:
            return ''

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix
