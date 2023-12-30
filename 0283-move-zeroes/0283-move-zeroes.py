class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nb_zeros = 0
        for i in range(len(nums)):
            if nums[i]==0:
                nb_zeros +=1
            else:
                nums[i-nb_zeros], nums[i] = nums[i], nums[i-nb_zeros]