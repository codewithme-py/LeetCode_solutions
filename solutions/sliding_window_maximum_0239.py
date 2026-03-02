from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the maximum values in each sliding window of size k.

        The algorithm uses a monotonic deque (double-ended queue) to achieve
        a time complexity of O(n), where n is the length of the nums array.

        The monotonic deque stores indices of elements in the nums array in
        descending order of their values. Thus, the element with index dq[0]
        is always the index of the maximum element in the current window.

        Args:
            nums (list[int]): Input array of integers.
            k (int): Size of the sliding window.

        Returns:
            list[int]: List of maximum values for each window.

        Example:
            >>> nums = [1, 3, -1, -3, 5, 3, 6, 7]
            >>> k = 3
            >>> Solution().maxSlidingWindow(nums, k)
            [3, 3, 5, 5, 6, 7]

        Time Complexity:
            O(n), where n is the length of nums. Each index is added and removed
            from the deque at most once.

        Space Complexity:
            O(k), as the deque stores at most k indices.
        """
        result, dq = [], deque()
        for i in range(len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
