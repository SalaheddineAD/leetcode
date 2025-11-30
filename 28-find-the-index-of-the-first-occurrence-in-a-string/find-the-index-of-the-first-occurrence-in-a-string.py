class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while i<= len(haystack)-len(needle):
            if haystack[i:len(needle)+i] ==needle:
                return i
            i +=1
        return -1
