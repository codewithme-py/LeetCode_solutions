class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generate all valid combinations of n pairs of parentheses.

        Uses backtracking: build combinations by adding '(' or ')'
        until the length reaches 2*n.

        Validity rules:
        - '(' can be added if open_count < n
        - ')' can be added if close_count < open_count

        Args:
            n: Number of pairs of parentheses (1 <= n <= 8)

        Returns:
            List of all valid combinations of parentheses

        Time Complexity: O(4^n / sqrt(n)) - Catalan number
        Space Complexity: O(n) - recursion depth
        """
        open_bracket, close_bracket = '(', ')'
        result: list[str] = []
        def backtrack(current: str, open_count: int, close_count: int) -> None:
            if len(current) == n * 2:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + open_bracket, open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + close_bracket, open_count, close_count + 1)
        backtrack('', 0, 0)
        return result
