class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        dic = {'{':'}',
                   '(':')',
                   '[':']'}
        for i in s:
            if i in dic.keys():
                lst.append(i)
            else:
                
                if len(lst)==0 or dic[lst.pop()]!=i:
                    return False
            
        if len(lst)==0:
            return True
        else: 
            return False
                
            