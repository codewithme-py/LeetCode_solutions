class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays.
        :param nums1: First sorted array
        :param nums2: Second sorted array
        :return: Median of the two sorted arrays
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            return self._median_single(nums2)
        return self._find_median_sorted_arrays(nums1, nums2)

    def _median_single(self, nums: list[int]) -> float:
        """
        Find the median of a single sorted array.
        :param nums: Sorted array
        :return: Median of the array
        """
        n = len(nums)
        if n % 2 == 1:
            return float(nums[n // 2])
        else:
            mid1 = nums[n // 2 - 1]
            mid2 = nums[n // 2]
            return (mid1 + mid2) / 2.0

    def _find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays using binary search.
        :param nums1: First sorted array (shorter)
        :param nums2: Second sorted array (longer)
        :return: Median of the two sorted arrays
        """
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        if m > n:
            return self._find_median_sorted_arrays(nums2, nums1)
        low, high = 0, m
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half_len - partition1
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            min_right1 = nums1[partition1] if partition1 < m else float('inf')
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            min_right2 = nums2[partition2] if partition2 < n else float('inf')
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total_len % 2 == 1:
                    return float(max(max_left1, max_left2))
                else:
                    return (
                        max(max_left1, max_left2) + min(min_right1, min_right2)
                        ) / 2.0
            elif max_left1 > min_right2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        raise ValueError('Input arrays are not sorted or invalid')
