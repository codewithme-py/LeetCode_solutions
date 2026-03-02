class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Given an array of positive integers nums and a positive integer target,
        return the minimal length of a contiguous subarray of which the sum is
        greater than or equal to target.
        If there is no such subarray, return 0.
        """
        left_mark, current_sum, min_length = 0, 0, float('inf')
        for right_mark in range(len(nums)):
            current_sum += nums[right_mark]
            while current_sum >= target:
                min_length = min(min_length, right_mark - left_mark + 1)
                current_sum -= nums[left_mark]
                left_mark += 1
        return 0 if min_length == float('inf') else min_length
