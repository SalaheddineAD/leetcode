class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i-k]==val:
                print(nums)
                nums.remove(val)
                print(nums)
                k+=1
        return n-k     