class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v =0
        i =0
        j = len(height)-1
        while (j>i):
            k=1
            volume = (j-i)*min(height[j],height[i])
            max_v = max(volume,max_v)
            
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return max_v