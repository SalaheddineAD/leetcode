class Solution:
    def trailingZeroes(self, n: int) -> int:
        result=0
        r=1
        while n>=5**r:
            result+=n//5**r
            r+=1
        return result