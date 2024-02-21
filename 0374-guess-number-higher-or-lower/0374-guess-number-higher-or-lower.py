# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        step = n//4
        num = n//2
        while guess(num)!=0:
            num=num +guess(num)*step
            step=max(step//2,1)
        
        return num
        
            