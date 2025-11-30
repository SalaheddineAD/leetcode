class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        l=0
        while i>=0:
            if s[i]== " ":
                i-=1
            else:
                break

        while i>=0:
            if s[i] == " ":
                return l
            l+=1
            i-=1
        return l