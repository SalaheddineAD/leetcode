class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        if n <1:
            return nums[0]
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] +=1
                if dic[i] >n:
                    return i
            else:
                dic[i]=1
        