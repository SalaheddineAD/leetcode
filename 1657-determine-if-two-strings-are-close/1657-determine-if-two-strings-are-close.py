class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1)!=len(word2):
            return False
        
        cnt_char1={}
        cnt_char2={}
        for i in word1:
            if i in cnt_char1.keys():
                cnt_char1[i]+=1
            else:
                cnt_char1[i]=1
        
        for i in word2:
            if i in cnt_char2.keys():
                cnt_char2[i]+=1
            else:
                cnt_char2[i]=1
        
        if sorted(list(cnt_char1.keys()))!= sorted(list(cnt_char2.keys())):
           return False
        if sorted(list(cnt_char1.values()))!= sorted(list(cnt_char2.values())):
           return False

        
        return True
            
            
            