class Solution:
    def reverseWords(self, s: str) -> str:
        
        splitList= s.split(" ")
        splitList = list(filter(lambda i: len(i)>0, splitList))
        splitList.reverse()
        return ' '.join(i for i in splitList)