class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nb_zeros = 0
        for i in range(len(nums)):
            if nums[i]==0:
                nb_zeros +=1
            elif nb_zeros >0:
                nums[i-nb_zeros]=nums[i]
                nums[i]=0