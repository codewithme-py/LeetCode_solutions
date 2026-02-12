class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Reformat string s in zigzag pattern with numRows rows,
        and then read it line by line.
        Args:
            s: Input string
            numRows: Number of rows
        Returns:
            Reformatted string
        Examples:
            >>> sol = Solution()
            >>> sol.convert("PAYPALISHIRING", 3)
            'PAHNAPLSIIGYIR'
            >>> sol.convert("PAYPALISHIRING", 4)
            'PINALSIGYAHRPI'
            >>> sol.convert("A", 1)
            'A'
        """
        if numRows == 1:
            return s
        rows = ['' for _ in range(numRows)]
        current_row = 0
        direction = 1
        for i in range(len(s)):
            rows[current_row] += s[i]
            current_row += direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
        return ''.join(rows)
