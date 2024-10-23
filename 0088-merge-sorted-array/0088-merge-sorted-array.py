class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        i = m - 1  # index of the last valid number in nums1
        j = n - 1  # index of the last number in nums2
        lastZero = m + n - 1  # index of the last position in nums1
        
        # Merge nums1 and nums2 from the end to the beginning
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[lastZero] = nums1[i]
                i -= 1
            else:
                nums1[lastZero] = nums2[j]
                j -= 1
            lastZero -= 1
