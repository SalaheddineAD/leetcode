class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst_0 = []
        prod=1
        for i in range(len(nums)):
            if nums[i] ==0:
                lst_0.append(i)
            else:
                prod*=nums[i]
        
        if len(lst_0)>1:
            return list(0 for i in range(len(nums)))
        elif len(lst_0)==1:
            result = list(0 for i in range(len(nums)))
            result[lst_0[0]]=prod
            return result
        
        return list(int(prod/i) for i in nums)