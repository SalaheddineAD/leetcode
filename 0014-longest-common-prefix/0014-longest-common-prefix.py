class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        
        for tmp in strs[1:]:
            if len(answer)>len(tmp):
                answer = answer[:len(tmp)]
                
            for i in range(len(answer)):
                if answer[i]!= tmp[i]:
                    answer = answer[:i]
                    break
            
                    
        return answer