class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        lst =[n-1]
        sum=0
        for i in range(n-2,-1,-1):
            for j in lst:
                if nums[i]+i>=j:
                    lst.insert(0,i)
                    break
        if 0 in lst:
            return True
        return False