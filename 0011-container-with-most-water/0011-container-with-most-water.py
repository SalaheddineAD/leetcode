class Solution:
    def maxArea(self, height: List[int]) -> int:
        max =0
        i =0
        j = len(height)-1
        while (j>i):
            k=1
            volume = (j-i)*min(height[j],height[i])
            max = volume if volume >max else max
            
            if height[j]>height[i]:
                # while i+k<j and height[i+k]-k<height[i]:
                #     k+=1
                # i+=k
                i+=1
            else:
                # while i+k<j and height[j-k]-k<height[j]:
                #     k+=1
                # j-=k
                j-=1
        return max