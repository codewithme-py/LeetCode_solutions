class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Return indices of the two numbers in `nums` that add up to `target`.
        Runs in O(n) time: traverses the list once, storing each number and its index
        in a dictionary. For each element, checks if the complement (`target - current`)
        has already been seen. If so, returns the pair of indices.
        Assumes exactly one valid solution exists.
        """
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        raise ValueError('Нет решения')
