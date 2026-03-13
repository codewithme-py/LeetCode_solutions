class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
        ) -> bool:
        """
        Look for two different indices i and j, where:
        1. |i - j| <= indexDiff  (indices are close)
        2. |nums[i] - nums[j]| <= valueDiff  (values are close)
        Args:
            nums (list[int]): Input array.
            indexDiff (int): Maximum distance between indices.
            valueDiff (int): Maximum distance between values.
        Returns:
            bool: True, if a suitable pair of indices is found, otherwise False.
        Time Complexity:
            O(n) — each element is processed once,
            checking 3 buckets = O(1).
        Space Complexity:
            O(min(n, indexDiff)) — we store at most indexDiff buckets.
        """
        if valueDiff < 0 or indexDiff <= 0:
            return False
        buckets = {}
        bucket_size = valueDiff + 1
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            if bucket_id in buckets:
                return True
            if (bucket_id - 1 in buckets
                and abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True
            if (bucket_id + 1 in buckets
                and abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True
            buckets[bucket_id] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
        return False
