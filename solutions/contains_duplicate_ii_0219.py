class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Function checks if there are duplicates in the array nums within k.
        set guarantees O(1) for addition and checking for existence.
        The size of set never exceeds k+1.
        Memory O(k)
        Time O(n)
        """
        window_set = set()
        for i in range(len(nums)):
            if nums[i] in window_set:
                return True
            window_set.add(nums[i])
            if i >= k:
                window_set.remove(nums[i - k])
        return False
