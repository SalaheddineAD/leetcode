class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        length=len(nums)
        if length==0:
            return []
        curr=nums[0]
        for i in range(1,length):
            if nums[i] == nums[i-1]+1:
                continue
            else:
                l.append([curr,nums[i-1]])
                curr = nums[i]
        l.append([curr,nums[length-1]])
        
        print(l)
        result=[]
        for pair in l:
            if pair[0]==pair[1]:
                result.append(str(pair[0]))
            else:
                result.append(str(pair[0])+"->"+str(pair[1]))
        return result
