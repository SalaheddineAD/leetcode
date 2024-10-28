class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_pos = 0
        jumps = 0
        max_reach = 0
        n = len(nums)
        
        for i in range(n-1):
            max_reach = max(max_reach, i+nums[i])
            if i == max_pos:
                max_pos = max_reach
                jumps+=1
            if max_pos>n-1:
                return jumps
        return jumps
                
                
                
            
            