class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        word1 = list(word1)
        word2 = list(word2)

        for i in range(min(len(word1),len(word2))):
            result.append(word1.pop(0))
            result.append(word2.pop(0))
        
        if len(word1)!=0:
            result+=word1
        elif len(word2)!=0:
            result+=word2
            
        return ''.join(str(i) for i in result)