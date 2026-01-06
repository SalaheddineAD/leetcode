import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if 0<=x<=2: return min(x,1)
        for i in range(x):
            if i*i == x:
                return i
            elif i*i<x:
                continue
            else:
                return i-1