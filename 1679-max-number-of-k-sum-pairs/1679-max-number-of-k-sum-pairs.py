class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        lst = []
        for i in nums:
            if k-i in lst:
                result+=1
                lst.remove(k-i)
            elif i<=k:
                lst.append(i)
        return result
                
                